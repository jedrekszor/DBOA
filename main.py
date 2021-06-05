from butterfly_swarm import ButterflySwarm
from determinant_swarm import DeterminantSwarm
from config import population, iterations, calculate_value, mark, precision, is_precision
import math
import matplotlib.pyplot as plt
import os
import time


start_time = time.time()
global_best = math.inf
results = []
for i in range(0, iterations):
    results.append(0)
for j in range(0, 30):
    determinant_swarm = DeterminantSwarm()
    butterfly_swarm = ButterflySwarm()
    best = math.inf
    if is_precision:
        if best < precision:
            break
    for i in range(0, iterations):
        determinant_swarm.step()
        butterfly_swarm.step(determinant_swarm.swarm)
        # av = 0
        #     av += calculate_value(butterfly.coordinates)
        if calculate_value(butterfly_swarm.best_butterfly.coordinates) < best:
            best = calculate_value(butterfly_swarm.best_butterfly.coordinates)
            if best < global_best:
                global_best = best
        # a = a_max * (1 - (i/iterations)/2)
        results[i] += best
        print("Cycle: {}, Iteration {}, best value: {}".format(j, i, best))
    print("################################")
for i in range(0, iterations):
    results[i] = results[i]/30
plt.plot(results)
if not os.path.isdir("raport/plots"):
    os.makedirs("raport/plots")
plt.savefig("raport/plots/{}.png".format(mark))
print("\nPlots saved, overall best: {}".format(global_best))
delta = time.time() - start_time
print("Execution time: {}m {}s".format(int(delta / 60), delta % 60))
