import sys

class Shoe(object):
    def __init__(self, brand, size):
        self.brand = brand
        if isinstance(size, int):
            self._size = size
        else:
            sys.stdout.write(u"size must be an integer\n")
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            sys.stdout.write(u"size must be an integer\n")
    
    def cobble(self):
        sys.stdout.write(u"Your shoe is as good as new!\n")
        self.condition = "New"