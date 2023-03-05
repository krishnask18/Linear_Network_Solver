from sympy import *
Nodelist = []
nodename = []

t = Symbol('t')

class Node:
    def __init__(self, name, volt = None):
        if volt == None:
            volt = Symbol(f'{name}v')
            Nodelist.append(self)
            nodename.append(name)
        else:
            try:
                volt = float(volt)
            except:
                volt = eval(volt)
        self.volt = volt
        self.name = name
        self.branches = []
    def print(self):
        print(f'Node {self.name} has {self.volt} voltage.')

solved = False

def SolveNodes():
    Eqnlist = []
    Jacobian = []
    for node in Nodelist:
        kcl = 0
        for crnt in node.branches:
            kcl += crnt
        Eqnlist.append(kcl)
    fmatrix = Matrix(Eqnlist)
    i = 0
    for node in Nodelist:
        ls = []
        for eqn in Eqnlist:
            der = diff(eqn, node.volt)
            ls.append(der)
        Jacobian.append(ls)
        i += 1
    Jacobian = Matrix(Jacobian)
    inv_jacobian = Jacobian**(-1)
    x0 = [0]*len(Nodelist)
    x0 = Matrix(x0)
    
    i = 0
    initguess = fmatrix
    initjac = inv_jacobian
    for node in Nodelist:
        initguess = initguess.subs(node.volt, x0[i])
        initjac = initjac.subs(node.volt, x0[i])
    i += 1
    for i in range(3):
        x1 = x0 - initjac*initguess
        x0 = x1
        i = 0
        initguess = fmatrix
        initjac = inv_jacobian
        for node in Nodelist:
            initguess = initguess.subs(node.volt, x0[i])
            initjac = initjac.subs(node.volt, x0[i])
            i += 1
    i = 0
    for node in Nodelist:
        node.__init__(node.name, str(x1[i]))
        try:
            node.volt.doit()
        except:
            node.volt = node.volt
        i += 1
    solved = True

gnd = Node('gnd', 0)