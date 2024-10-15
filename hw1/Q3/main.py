import numpy as np
import logging
import pandas as pd

class OneMaxSolver(object):
    def __init__(self, bits:int, num_of_populations :int, num_of_generations:int, cross_probablity: float):
        self.bits = bits
        self.num_of_populations = num_of_populations
        self.num_of_generations = num_of_generations
        self.cross_probablity = cross_probablity
        self.infos = pd.DataFrame(columns=["generation", "max_fitness", "mean_fitness", "min_fitness", "std_fitness"]) 
        self.random_init_populations()
        logging.info(f"Initial populations size: {self.population.shape}")
        print(self.evaluate_fitness(self.population))

    def random_init_populations(self):
        self.population = np.random.randint(0 , 2,size = (self.num_of_populations, self.bits))
        self.reocrd_infos(0)

    def reocrd_infos(self, generation):
        fitness = self.evaluate_fitness(self.population)
        new_row = {
            "generation": generation,
            "max_fitness": np.max(fitness),
            "mean_fitness": np.mean(fitness),
            "min_fitness": np.min(fitness),
            "std_fitness": np.std(fitness)
        }

        self.infos.loc[len(self.infos)] = new_row

    def evaluate_fitness(self, population):
        return np.sum(population, axis=1)

    def get_info(self):
        return self.infos

def main():
    logging.basicConfig(level=logging.INFO)
    bits = 50
    num_of_populations = 200
    num_of_generations = 100
    crossover_probablity = 1.0
    runs = 10
    for i in range(runs):
        onemax = OneMaxSolver(bits, num_of_populations, num_of_generations, crossover_probablity)
        infos = onemax.get_info()
        print(infos)
        logging.info(f"Run {i} finished")
    logging.info("All runs finished")        

if __name__ == "__main__":
    main()
