from typing import Union
import random


class ColorItems:
    total_dict: dict[int: str] = {}

    def __init__(self):

        self.blue: int = random.randint(70, 75)
        self.green: int = 90 - self.blue
        self.red: int = 10

        blue: int = self.blue
        green: int = self.green

        for i in range(1, 101):
            if blue != 0:
                self.total_dict[i] = 'blue'
                blue -= 1

            elif green != 0:
                self.total_dict[i] = 'green'
                green -= 1

            else:
                self.total_dict[i] = 'red'


class Sqrt:
    def __init__(self, a, b, c):
        self.a: int = a
        self.b: int = b
        self.c: int = c
        self.discriminant: int = (self.b ** 2) - (4 * self.a * self.c)
        self.sqrt1: Union[float, None] = None
        self.sqrt2: Union[float, None] = None

    def find_square(self):
        if self.discriminant > 0:
            self.sqrt1 = round((-self.b + self.discriminant ** .5) / (2 * self.a), 2)
            self.sqrt2 = round((-self.b - self.discriminant ** .5) / (2 * self.a), 2)

        if self.discriminant == 0:
            self.sqrt1 = round(-self.b / 2 * self.a, 2)

        return self.sqrt1, self.sqrt2
