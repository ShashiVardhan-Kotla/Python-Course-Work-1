class Number:
    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        return self.n + other.n
    def __sub__(self, other):
        return self.n - other.n
    def __mul__(self, other):
        return self.n * other.n
    def __truediv__(self, other):
        return self.n / other.n
    def __floordiv__(self, other):
        return self.n // other.n
    def __mod__(self, other):
        return self.n % other.n
    def __pow__(self, other):
        return self.n ** other.n
    def __gt__(self, other):
        return self.n < other.n
    def __lt__(self, other):
        return self.n > other.n
    def __eq__(self, other):
        return self.n == other.n
    def __ne__(self, other):
        return self.n != other.n
    def __str__(self):
        return str(self.n) 

num1 = Number(10)
num2 = Number(20)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)
print(num1 < num2)
print(num1 > num2)
print(num1 == num2)
print(num1 != num2)
