from config import population
from butterfly import Butterfly


class ButterflySwarm:
    def __init__(self):
        self.swarm = []
        self.operational_swarm = []
        for i in range(0, population):
            self.swarm.append(Butterfly())
        self.best_butterfly = self.swarm[0]

    def select_best(self):
        self.best_butterfly = self.operational_swarm[0]
        for butterfly in self.operational_swarm:
            butterfly.calculate_fragrance()
            if butterfly.fragrance > self.best_butterfly.fragrance:
                self.best_butterfly = butterfly

    def move(self):
        for butterfly in self.operational_swarm:
            butterfly.move(self.best_butterfly, self.operational_swarm)

    def step(self, determinant_swarm):
        self.operational_swarm = self.swarm + determinant_swarm
        self.select_best()
        self.move()
