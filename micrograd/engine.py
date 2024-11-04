import numpy as np

class Value:
    def __init__(self, data):
        self.data = data

    # this is so that it prints the value of the data instead of the object address
    def __repr__(self) -> str:
        return f"Value(data={self.data}"
    
    # overloading methods, python interprets the + operator as a call to the __add__ method
    def __add__(self, other):
        return Value(self.data + other.data)
    
    def __mul__(self, other):
        return Value(self.data * other.data)
    

a = Value(3.0)
b = Value(4.0)
d = Value(5.0)
c = a + b * d
print(c)
