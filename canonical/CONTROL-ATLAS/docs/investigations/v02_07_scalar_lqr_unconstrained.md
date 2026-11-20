# Investigation 07. A stabilizing LQR gain can demand impossible input

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

For `x[k+1]=a*x[k]+b*u[k]` with a=1.2, b=1 and weights q=r=1, solve the scalar discrete algebraic Riccati equation and compute the stabilizing gain. The nominal closed-loop pole falls inside the unit circle. The mathematical result solves the stated infinite-horizon quadratic problem, not a constrained optimal-control problem. If the plant has limited actuator range, the commanded `u=-K*x` may be unavailable at a large state error.

The weights are choices reflecting a design objective, not automatically discovered values about the importance of comfort, reliability, cost or safety. Varying r changes the controller's willingness to use effort. The plant parameters themselves may change with temperature, load or wear. A real design needs uncertainty, feasibility, actuator limits and independent protection.

**Sources:** MIT Underactuated Robotics LQR chapter and python-control `dlqr`. **Refusal:** no hardware gain is recommended by this synthetic test.
