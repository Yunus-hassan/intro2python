class Animal:
    def __init__(self, name):
        self.name = name

    def makesound(self):
        pass


class Cat(Animal):
    def makesound(self):
        print("meow")


cat1 = Cat("tom")
cat1.makesound()
