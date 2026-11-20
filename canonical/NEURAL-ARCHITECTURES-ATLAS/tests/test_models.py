"""Independent invariants and constructed counterexamples; standard-library only."""
import math,random,unittest,tempfile,sys
from pathlib import Path
from neural_atlas.mathcore import matmul,transpose,stable_softmax,logsumexp,layer_norm
from neural_atlas.attention import attention
from neural_atlas.mlp import forward,loss_and_grads,sgd_step
from neural_atlas.quantization import quantize_int8,dequantize

class MatrixTests(unittest.TestCase):
    def test_shape(self):self.assertEqual(matmul([[1,2],[3,4]],[[5,6],[7,8]]),[[19,22],[43,50]])
    def test_identity(self):self.assertEqual(matmul([[2.5,-3],[0,4]],[[1,0],[0,1]]),[[2.5,-3],[0,4]])
    def test_transpose(self):self.assertEqual(transpose([[1,2,3],[4,5,6]]),[[1,4],[2,5],[3,6]])
    def test_mismatch(self):
        with self.assertRaises(ValueError):matmul([[1,2]],[[1,2]])
    def test_ragged(self):
        with self.assertRaises(ValueError):matmul([[1],[1,2]],[[2]])
    def test_nonfinite(self):
        with self.assertRaises(ValueError):matmul([[math.nan]],[[1]])
    def test_associativity_constructed(self):
        a=[[1,2],[3,4]];b=[[2,0],[-1,2]];c=[[3],[5]]
        self.assertEqual(matmul(matmul(a,b),c),matmul(a,matmul(b,c)))

class ProbabilityTests(unittest.TestCase):
    def test_extreme_stability(self):
        p=stable_softmax([10000,10000,9999]);self.assertAlmostEqual(sum(p),1,places=14)
        self.assertTrue(all(math.isfinite(v) for v in p))
    def test_shift_invariance(self):
        a=stable_softmax([1,3,5]);b=stable_softmax([501,503,505])
        for x,y in zip(a,b):self.assertAlmostEqual(x,y,places=13)
    def test_mask(self):self.assertEqual(stable_softmax([6,600,6],[True,False,True]),[.5,0,.5])
    def test_all_masked(self):
        with self.assertRaises(ValueError):stable_softmax([0,1],[False,False])
    def test_mask_width(self):
        with self.assertRaises(ValueError):stable_softmax([0,1],[True])
    def test_lse(self):self.assertAlmostEqual(logsumexp([1001,1001]),1001+math.log(2),places=10)
    def test_lse_invalid(self):
        with self.assertRaises(ValueError):logsumexp([math.inf])

class AttentionTests(unittest.TestCase):
    def test_one_token(self):self.assertEqual(attention([[2,1]],[[1,3]],[[9,-5]])[0],[[9,-5]])
    def test_uniform_weights(self):
        out,p=attention([[0,0]],[[1,0],[-1,0]],[[2,4],[6,8]])
        self.assertEqual(out,[[4,6]]);self.assertEqual(p,[[.5,.5]])
    def test_causal_future_not_visible(self):
        q=[[1,0],[0,1]];k=[[1,0],[0,1]]
        a,p=attention(q,k,[[2],[4]],causal=True)
        b,_=attention(q,k,[[2],[400]],causal=True)
        self.assertEqual(a[0],b[0]);self.assertEqual(p[0],[1,0])
    def test_causal_requires_square_sequence(self):
        with self.assertRaises(ValueError):attention([[1]],[[1],[2]],[[3],[4]],causal=True)
    def test_wrong_feature_width(self):
        with self.assertRaises(ValueError):attention([[1,2]],[[1]],[[1]])
    def test_probability_rows(self):
        _,p=attention([[1,0],[0,1]],[[1,0],[0,1]],[[2],[4]])
        self.assertTrue(all(abs(sum(row)-1)<1e-12 for row in p))

class NormalizationTests(unittest.TestCase):
    def test_constant(self):self.assertEqual(layer_norm([3,3,3]),[0,0,0])
    def test_centered(self):self.assertAlmostEqual(sum(layer_norm([1,2,3,4])),0,places=13)
    def test_scale_affine(self):
        norm=layer_norm([1,2,3],gamma=[2,2,2],beta=[3,3,3]);base=layer_norm([1,2,3])
        for a,b in zip(norm,base):self.assertAlmostEqual(a,2*b+3,places=12)
    def test_invalid_eps(self):
        with self.assertRaises(ValueError):layer_norm([1],eps=0)

class GradientTests(unittest.TestCase):
    def setUp(self):
        self.x=[.4,-.2];self.target=.7;self.w1=[[.3,-.1],[-.2,.5]];self.b1=[.1,-.3];self.w2=[.7,-.4];self.b2=.2
    def test_nonnegative_loss(self):self.assertGreaterEqual(loss_and_grads(self.x,self.target,self.w1,self.b1,self.w2,self.b2)[0],0)
    def test_finite_difference_all_parameters(self):
        _,g=loss_and_grads(self.x,self.target,self.w1,self.b1,self.w2,self.b2)
        h=1e-6
        for group,values in [('w1',self.w1),('b1',self.b1),('w2',self.w2)]:
            for i,x in enumerate(values):
                for j in (range(len(x)) if isinstance(x,list) else [None]):
                    idx=(i,j) if j is not None else (i,)
                    def altered(shift):
                        vv=[list(row) if isinstance(row,list) else row for row in values]
                        if j is None:vv[i]+=shift
                        else:vv[i][j]+=shift
                        return vv
                    def loss(shift):
                        xs={'w1':self.w1,'b1':self.b1,'w2':self.w2};xs[group]=altered(shift)
                        return loss_and_grads(self.x,self.target,xs['w1'],xs['b1'],xs['w2'],self.b2)[0]
                    approx=(loss(h)-loss(-h))/(2*h)
                    gradient=g[group][i][j] if j is not None else g[group][i]
                    self.assertAlmostEqual(approx,gradient,delta=1e-8)
        def bias_loss(t):return loss_and_grads(self.x,self.target,self.w1,self.b1,self.w2,t)[0]
        self.assertAlmostEqual((bias_loss(self.b2+h)-bias_loss(self.b2-h))/(2*h),g['b2'],delta=1e-8)
    def test_small_step_decreases_loss(self):
        before,nw1,nb1,nw2,nb2=sgd_step(self.x,self.target,self.w1,self.b1,self.w2,self.b2,.01)
        after,_=loss_and_grads(self.x,self.target,nw1,nb1,nw2,nb2)
        self.assertLess(after,before)
    def test_bad_learning_rate(self):
        with self.assertRaises(ValueError):sgd_step(self.x,self.target,self.w1,self.b1,self.w2,self.b2,-.1)
    def test_mismatch(self):
        with self.assertRaises(ValueError):forward([1,2],[[3]],[0],[1],0)

class QuantTests(unittest.TestCase):
    def test_zero(self):self.assertEqual(quantize_int8([0,0]),(1.0,[0,0]))
    def test_range_and_peak(self):
        s,q=quantize_int8([-9,0,9]);self.assertEqual(q,[-127,0,127]);self.assertEqual(dequantize(s,q),[-9,0,9])
    def test_absolute_error_bound(self):
        values=[-10,-7,-.1,0,.7,3,10];s,q=quantize_int8(values)
        self.assertTrue(all(abs(v-x)<=s/2+1e-12 for v,x in zip(values,dequantize(s,q))))
    def test_nonfinite(self):
        with self.assertRaises(ValueError):quantize_int8([math.inf])
    def test_invalid_code(self):
        with self.assertRaises(ValueError):dequantize(1.0,[128])

if __name__=='__main__':unittest.main()
