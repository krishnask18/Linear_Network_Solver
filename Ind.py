from Node import *
import sympy as sm

class Inductor():
    def __init__(self, name, n1, n2, L):
        self.i = (-1/float(L))*(sm.integrate((n1.volt - n2.volt), t))
        try:
            self.i.doit()
        except:
            self.i = self.i
        self.name = name
        self.res = (n1.volt - n2.volt)/self.i
        n1.branches.append(self.i)
        n2.branches.append(-self.i)
    def print(self, time):
        if solved == True:
            self.__init__(self, self.name, self.n1, self.n2, self.L)
        print(f'Inductor {self.name} has {simplify(self.i.subs(t, time))} current at time {time}')


A = Node('A', '4*sin(t)')
C = Node('C')
B = gnd

L1 = Inductor('L1', A, B, 2)
L2 = Inductor('L2', A, C, 1)
L3 = Inductor('L3', C, B, 1)
SolveNodes()
L1 = Inductor('L1', A, B, 2)
L2 = Inductor('L2', A, C, 1)
L3 = Inductor('L3', C, B, 1)
L1.print(t)
L2.print(t)
C.print()