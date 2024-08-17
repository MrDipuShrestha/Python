class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Enhale, Exhale")
# fish class inherit the animal class
class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Under the water.")
    def eat(self):
        print("Eat a food.")

nemo = Fish()
nemo.breathe()
nemo.eat()