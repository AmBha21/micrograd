import numpy as np

class Value:
    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return f"Value(data={self.data}"
    
a = Value(3.0)
b = Value(4.0)
c = a + b
