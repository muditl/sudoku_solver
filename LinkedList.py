import numpy as np


class LinkedList:
    def __init__(self, element=None):
        self.container = []
        if element is not None:
            if len(element) != 3:
                raise Exception("Invalid Argument. Expected length 3, got{}".format((str(len(element)))))
            self.container.append(element)

    def __add__(self, element):
        if element is None:
            raise Exception("Element is None.")
        if len(element) != 3:
            raise Exception("Invalid Argument. Expected length 3, got{}".format((str(len(element)))))
        self.container.append(element)

    def get_first(self):
        if self.__sizeof__() < 1:
            raise Exception("List is empty.")
        return self.container[0]

    def get__all(self):
        return self.container

    def remove_first(self):
        if self.__sizeof__() < 1:
            raise Exception("List is empty.")
        element = self.get_first()
        self.container.remove(element)
        return element

    def reorder(self, order):
        if len(order) != self.__sizeof__():
            raise Exception("List and order do not have the same number of elements")
        new_cont = np.zeros((self.__sizeof__(), 3), dtype=int)
        for i in range(len(order)):
            if order[i] >= self.__sizeof__():
                raise Exception("Requested positions is Out Of Bounds.")
            new_cont[i] = self.container[order[i]]
        self.container = new_cont

    def __sizeof__(self):
        return len(self.container)

    def __str__(self):
        res = "["
        for i in range(len(self.get__all())):
            res += self.get__all()[i].__str__()
            if i < self.__sizeof__() - 1:
                res += ", "
        res += "]"
        return res
