class Dog:
    def __init__(self, name, age, hunger=0, happynes=10):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.happynes = happynes

    def description(self):
        self.hunger += 1
        self.happynes -= 1
        return " {} is {} years old, and its hunger state is {} and its happines is {}"\
            .format(self.name, self.age, self.hunger, self.happynes)

    def feed(self):
        self.hunger += 1



dog1 = Dog("Dino", 7)
dog2 = Dog("Mila", 1)


print(dog1.description())
dog1.feed()
print(dog1.description())
