from config import determinants, dimensions, calculate_value, mutation, domain
from determinant import Determinant
from random import random
from copy import deepcopy


class DeterminantSwarm:
    def __init__(self):
        self.swarm = []
        self.operating_swarm = []
        for i in range(0, determinants):
            self.swarm.append(Determinant())
        self.best = self.swarm[0]

    def select_best(self):
        self.best = self.operating_swarm[0]
        for determinant in self.operating_swarm:
            if calculate_value(determinant.coordinates) < calculate_value(self.best.coordinates):
                self.best = determinant

    def cross_breed(self):
        for determinant in self.operating_swarm:
            temp = Determinant()
            for i in range(0, dimensions):
                r = random()
                temp.coordinates[i] = determinant.coordinates[i] * r + self.best.coordinates[i] * (1 - r)
            if calculate_value(temp.coordinates) < calculate_value(determinant.coordinates):
                determinant.coordinates = temp.coordinates

    def mutate(self):
        for determinant in self.operating_swarm:
            for i in range(0, dimensions):
                if random() < mutation:
                    determinant.coordinates[i] = random() * domain * 2 - domain

    def validate(self):
        for i in range(0, determinants):
            if calculate_value(self.operating_swarm[i].coordinates) > calculate_value(self.swarm[i].coordinates):
                self.operating_swarm[i] = self.swarm[i]
        self.swarm = self.operating_swarm

    def step(self):
        self.operating_swarm = deepcopy(self.swarm)
        self.select_best()
        self.cross_breed()
        self.mutate()
        self.validate()
