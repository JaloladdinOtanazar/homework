
import math
class Vector:
    def __init__(self, *args):
        self.args = list(args)
    
    def __repr__(self):
        return f"Vector({', '.join(map(str, self.args))})"

    def __len__(self):
        return len(self.args)
        
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be in a same dimention")
        addition = [x + y for x, y in zip(self.args, other.args)]
        return Vector(*addition)
    
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be in a same dimention")
        substraction = [x - y for x, y in zip(self.args, other.args)]
        return Vector(*substraction)
    def __mul__(self, other):   
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must be in a same dimention")
            dot_product = sum(x*y for x, y in zip(self.args, other.args))
            return Vector(*dot_product)
        elif isinstance(other, (int, float)):
            print("this is a scalar product, because one of them is a number")
            scalar_product = [ x*other for x in other.args]
            return Vector(*scalar_product)
        else:
            raise TypeError("Innappropriate argument type")
    def magnitude(self):
        return math.sqrt(sum(x**2 for x in self.args))
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        norm = [round(x/mag, 3) for x in self.args]
        return Vector(*norm)
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = v1 + v2
print(v3)
v_unit = v1.normalize()
print(v_unit)  

 
    

    