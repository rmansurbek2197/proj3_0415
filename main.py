# 6
class Power2:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return self.n ** 2

print(Power2(int(input())).solve())

# 7
class Power3:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return self.n ** 3

print(Power3(int(input())).solve())

# 8
class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def solve(self):
        return self.a // self.b

a, b = map(int, input().split())
print(Division(a, b).solve())

# 9
class Modulus:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def solve(self):
        return self.a % self.b

a, b = map(int, input().split())
print(Modulus(a, b).solve())

# 10
class ReverseNum:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return int(str(self.n)[::-1])

print(ReverseNum(int(input())).solve())
