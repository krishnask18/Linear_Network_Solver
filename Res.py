from Node import *

resilist = []

class Resistor:
    def __init__(self, name, n1, n2, value = None, current = None):
        if value == None:
            if current != None:
                value = (n1.volt - n2.volt)/float(current)
            else:
                value = Symbol(f'val{name}')
                current = (n1.volt - n2.volt)/value
        elif value != None:
            if current == None:
                current = (n1.volt - n2.volt)/float(value)
        for nd in Nodelist:
            if n1 == nd or n2 == nd:
                resilist.append(self)
        n1.branches.append(current)
        n2.branches.append(-current)
        self.name = name
        self.value = value
        self.current = current
        self.n1 = n1
        self.n2 = n2
    def print(self):
        print(f'Resistor {self.name} has value ({self.value})ohm and ({self.current})A current flows in it.')