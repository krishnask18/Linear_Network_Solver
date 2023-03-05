from Node import *
import sympy as sm

class Capacitor():
    def __init__(self, name, n1, n2, C):
        self.i = (-float(C))*(sm.diff((n1.volt - n2.volt), t))
        try:
            self.i.doit()
        except:
            self.i = self.i
        self.name = name
        self.res = (n1.volt - n2.volt)/self.i
        n1.branches.append(self.i)
        n2.branches.append(-self.i)
    def print(self, time):
        print(f'Capacitor {self.name} has {simplify(self.i.subs(t, time))} current at time {time}')

A = Node('A', '4*sin(t)')
C = Node('C')
B = gnd

C1 = Capacitor('C1', A, B, 2)
C2 = Capacitor('C2', A, C, 1)
C3 = Capacitor('C3', C, B, 1)
C2.print(t)
SolveNodes()
C1 = Capacitor('C1', A, B, 2)
C2 = Capacitor('C2', A, C, 1)
C3 = Capacitor('C3', C, B, 1)
C1.print(t)
C2.print(t)
C.print()