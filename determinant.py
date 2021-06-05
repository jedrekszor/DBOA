from config import dimensions, domain, calculate_value, a, c
from random import random


class Determinant:
    def __init__(self):
        self.fragrance = None
        self.coordinates = []
        for i in range(0, dimensions):
            self.coordinates.append(random() * domain * 2 - domain)

    def calculate_fragrance(self):
        I = 1 / calculate_value(self.coordinates)
        self.fragrance = c * pow(I, a)

    def move(self, best_butterfly, butterflies):
        pass
