# Linear_Network_Solver

Created a tool to solve passive circuit elements such as resistor capacitor and inductor to find current through and node voltages in the circuit.

Circuit elements are created as instances of respective class with input as in which nodes it is present and its value (resistance/capacitance/inductance).
Initially nodes must be created to insert elements in between.
SolveNodes() is a function which finds unknown node voltages by solving branch currnets using Kirchoff's Current Law.
SolveNodes() function uses Newton-Raphson method to solve KCL equations.
Finally one can print current through any element or any node voltage in respective circuit.
