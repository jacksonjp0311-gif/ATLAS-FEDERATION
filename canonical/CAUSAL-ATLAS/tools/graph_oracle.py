"""Optional separate-algorithm comparison; not independent scientific review."""
from pathlib import Path
from itertools import combinations
import sys,json,platform,random
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from causal_atlas.models import DAG

def run():
    try:import networkx as nx
    except ImportError:return {'result':'not_run','reason':'Optional NetworkX dependency unavailable'}
    failures=[];checks=0
    names=('A','B','C','D');possible=list(combinations(names,2))
    for mask in range(1<<len(possible)):
        edges=[e for i,e in enumerate(possible) if mask&(1<<i)]
        graph=DAG(names,edges);other=nx.DiGraph();other.add_nodes_from(names);other.add_edges_from(edges)
        for a,b in combinations(names,2):
            remaining=[n for n in names if n not in (a,b)]
            for bits in range(1<<len(remaining)):
                z={n for i,n in enumerate(remaining) if bits&(1<<i)}
                local=graph.d_separated([a],[b],z);reference=nx.is_d_separator(other,{a},{b},z);checks+=1
                if local!=reference:failures.append({'edges':edges,'x':a,'y':b,'z':sorted(z)})
    exhaustive=checks;rng=random.Random(121126)
    names=tuple('N'+str(i) for i in range(7));possible=list(combinations(names,2))
    for _ in range(100):
        edges=[e for e in possible if rng.random()<.3]
        graph=DAG(names,edges);other=nx.DiGraph();other.add_nodes_from(names);other.add_edges_from(edges)
        for _ in range(10):
            a,b=rng.sample(names,2);z={n for n in names if n not in (a,b) and rng.random()<.4}
            local=graph.d_separated([a],[b],z);reference=nx.is_d_separator(other,{a},{b},z);checks+=1
            if local!=reference:failures.append({'edges':edges,'x':a,'y':b,'z':sorted(z)})
    return {'result':'passed' if not failures else 'failed','exhaustive_forward_order_four_node_graphs':64,
      'four_node_comparisons':exhaustive,'seeded_seven_node_comparisons':checks-exhaustive,'total_comparisons':checks,
      'seed':121126,'failures':failures,'oracle':'NetworkX is_d_separator','networkx_version':nx.__version__,
      'local_algorithm':'ancestral_moral_graph','independent_human_review':False,'causal_graph_truth_validated':False,
      'python':platform.python_version()}
if __name__=='__main__':
    r=run();print(json.dumps(r,indent=2));raise SystemExit(0 if r['result']=='passed' else 2)
