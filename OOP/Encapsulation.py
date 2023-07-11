class Base:
    def __init__(self):
        self.a = "i have rights"
        self.c = "and priviledges"

class Derived(Base):
    def __init__(self):
        print(self.a)
        print(self.c)

#create an instance of the parent class

obj1 =  Base()
print(obj1.a)
print(obj1.c)