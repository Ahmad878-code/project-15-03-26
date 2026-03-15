class Animal:
    def __init__(self, age):
        self.age = age

    def setage(self, age):
        self.age = age

    def getage(self):
        return self.age
    
    def __add__(self, predict):
        return Animal(self.age + predict.age)

    def __gt__(self, predict):
        return self.age > predict.age

    def __lt__(self, predict):
        return self.age < predict.age

    def __str__(self):
        return "combined age of two animals " + str(self.age)


c1 = Animal(5)
print(c1.getage())

c2 = Animal(6)
print(c2.getage())

c3 = c1 + c2
print(c3.getage())

print(c3 > c2)
print(c1 < c2)

print(c3)