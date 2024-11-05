import numpy as np

class Value:
    def __init__(self, data, children=(), op=''):
        self.data = data
        self.prev = set(children)
        self.op = op

    # prints the value of the data instead of the object address
    def __repr__(self) -> str:
        return f"Value(data={self.data}"
    
    # overloading methods, python interprets the + operator as a call to the __add__ method
    def __add__(self, other):
        return Value(self.data + other.data, (self, other), '+')
    
    def __mul__(self, other):
        return Value(self.data * other.data, (self, other), '*')
    

a = Value(3.0)
b = Value(4.0)
d = Value(5.0)
c = a + b * d
print(c.prev)
