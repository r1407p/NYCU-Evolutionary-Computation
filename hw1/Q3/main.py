import numpy as np
import logging
import pandas as pd

class OneMaxSolver(object):
    def __init__(self, bits:int, num_of_populations :int, num_of_generations:int, cross_probablity: float):
        self.bits = bits
        self.num_of_populations = num_of_populations
        self.num_of_generations = num_of_generations
        self.cross_probablity = cross_probablity
        self.random_init_populations()
        self.infos = pd.DataFrame(columns=["generation", "max_fitness", "mean_fitness", "min_fitness", "std_fitness"]) 
        logging.info(f"Initial populations size: {self.population.shape}")

    def random_init_populations(self):
        self.population = np.random.randint(0 , 2,size = (self.num_of_populations, self.bits))

def main():
    logging.basicConfig(level=logging.INFO)
    bits = 50
    num_of_populations = 200
    num_of_generations = 100
    crossover_probablity = 1.0
    onemax = OneMaxSolver(bits, num_of_populations, num_of_generations, crossover_probablity)

if __name__ == "__main__":
    main()
