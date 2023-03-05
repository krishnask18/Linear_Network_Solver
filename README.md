# Linear_Network_Solver

Created a tool to solve passive circuit elements such as resistor capacitor and inductor to find current through and node voltages in the circuit.
Seperate file for each element is uploaded in repository.
## Circuit Elements
Initially nodes must be created to insert elements in between.
Circuit elements are created as instances of respective class with input as its end nodes and its value (resistance/capacitance/inductance).
## Finding Currents
Current through Resistor is found by just dividing volatage difference by its value. For Inductor, current is obtained by integral of voltage difference w.r.t. time
and dividing by L. In case of capacitor, first differnetiate voltage diff w.r.t. time and multiply it by value of capacitance.
## Generation and Solving Equations
Kirchoff's current Law is used to generate list of equations obtained by appending currnet through each branch.
SolveNodes() is a function which finds unknown node voltages by solving branch currnets by solving equations obtained by KCL.
SolveNodes() function uses Newton-Raphson method to solve KCL equations.

Finally one can print current through any element or any node voltage in respective circuit.
