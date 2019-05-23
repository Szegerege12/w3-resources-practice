"""Write a Python program to get a dictionary from an object's fields."""

class DictObj(object):
    def __init__(self):
        self.a = 'red'
        self.y = 'green'
        self.b = 'purple'

    def do_nothing(self):
        pass


test = DictObj()
print(test.__dict__)
