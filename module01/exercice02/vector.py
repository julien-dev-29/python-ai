class Vector:
    """ A class representing a mathematical vector in 2D space. """
    
    def __init__(self, values: list[list[float]], shape: tuple[int] = None ):
        self.values = values
        self.shape = shape if shape is not None else (len(values), 1 if len(values) > 1 else len(values[0]))

    def __add__(self, other):
        if self.shape == other.shape:
            if len(self.values) > 1:
                for elem in self.values:
                    result.append([elem[0] * scalar])

            else:
                for elem in self.values[0]:
                    result.append(elem * scalar)
                result = [result]

    def __mul__(self, scalar):
        result = []

        if len(self.values) > 1:
            for elem in self.values:
                result.append([elem[0] * scalar])

        else:
            for elem in self.values[0]:
                result.append(elem * scalar)
            result = [result]
            
        return Vector(result)

    def __truediv__(self, scalar):
        try:
            if scalar == 0:
                raise ZeroDivisionError
            result = []

            if len(self.values) > 1:
                for elem in self.values:
                    result.append([elem[0] / scalar])

            else:
                for elem in self.values[0]:
                    result.append(elem / scalar)
                result = [result]

            return Vector(result)
        
        except ZeroDivisionError:
            print("ZeroDivisionError: division by zero.")

    def __rtruediv__(self, other):
        try:
            raise NotImplementedError
        except NotImplementedError:
            print("NotImplementedError: Division of a scalar by a vector is not defines here.")
    
    def __str__(self):
        return f"Vector({self.values})"