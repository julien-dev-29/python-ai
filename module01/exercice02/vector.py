class Vector:
    """ A class representing a mathematical vector in 2D space. """
    
    def __init__(self, values):

        if isinstance(values, list):
            self.values = values

        elif isinstance(values, int):
            self.values = [[float(i) for i in range(values)]]

        elif isinstance(values, tuple):
            self.values = [[float(i)] for i in range(values[0], values[1])]

        else:
            raise TypeError("Invalid vector inittialization.")

        if not self.values:
            raise ValueError("A vector cannot be empty.")

        if not all(isinstance(row, list) for row in self.values):
            raise ValueError("Vector elements must be lists.")

        if len(self.values) > 1 and any(len(row) != 1 for row in self.values):
            raise ValueError("Invalid column vector.")

        if len(self.values) == 1 and len(self.values[0]) == 0:
            raise ValueError("A vector cannot be empty.")
        
        self.shape = (len(self.values), 1 if len(self.values) > 1 else len(self.values[0]))
            
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        if self.shape != other.shape:
            raise ValueError("You can't add vectors of different shapes.")
        
        result = []

        if len(self.values) > 1:
            for i in range(len(self.values)):
                result.append([self.values[i][0] + other.values[i][0]])

        else:
            for i in range(len(self.values[0])):
                result.append(self.values[0][i] + other.values[0][i])
            result = [result]

        return Vector(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        if self.shape != other.shape:
            raise TypeError("You can't substract vectors of different shapes.")
        
        result = []

        if len(self.values) > 1:
            for i in range(len(self.values)):
                result.append([self.values[i][0] - other.values[i][0]])

        else:
            for i in range(len(self.values[0])):
                result.append(self.values[0][i] - other.values[0][i])
            result = [result]

        return Vector(result)

    def __rsub__(self, other):
        if isinstance(other, Vector):
            return other.__sub__(self)
        return NotImplemented

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

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, scalar):
            if scalar == 0:
                raise ZeroDivisionError("Division by zero.")

            result = []

            if len(self.values) > 1:
                for elem in self.values:
                    result.append([elem[0] / scalar])

            else:
                for elem in self.values[0]:
                    result.append(elem / scalar)
                result = [result]

            return Vector(result)

    def __rtruediv__(self, other):
        return NotImplemented
    
    def __str__(self):
        return f"Vector({self.values})"