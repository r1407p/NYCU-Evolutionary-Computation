import numpy as np
import random
import pandas as pd


class EvolutionStrategy:
    def __init__(self, sigma, strategy_type, max_iterations=10_000_000, target=0.005, n=10):
        """
        Initialize the parameters for the evolution strategy.
        
        :param sigma: Step-size for Gaussian mutation
        :param strategy_type: Type of evolution strategy ('comma' for (1, 1)-ES, 'plus' for (1 + 1)-ES)
        :param max_iterations: Maximum iterations allowed
        :param target: Target objective function value
        :param n: Dimension of the sphere model
        """
        self.sigma = sigma
        self.strategy_type = strategy_type
        self.max_iterations = max_iterations
        self.target = target
        self.n = n
        self.initial_solution = np.ones(n)  # Starting point (1, 1, ..., 1)

    def evaluate_fitness(self, x):
        """Sphere function: f(x) = sum(x_i^2)"""
        return np.sum(x ** 2)

    def mutate(self, x):
        """Apply Gaussian mutation with fixed step size."""
        offspring = x.copy()
        for i in range(self.n):
            offspring[i] += random.gauss(0, self.sigma)
        return offspring
        
    def run(self):
        """Run the evolution strategy and return the number of iterations to meet the target."""
        x = self.initial_solution
        best_fitness = self.evaluate_fitness(x)
        iterations = 0

        while best_fitness > self.target and iterations < self.max_iterations:
            # print(f"Iteration: {iterations}, Best fitness: {best_fitness}")
            iterations += 1
            candidate = self.mutate(x)
            parent_fitness = self.evaluate_fitness(x)
            candidate_fitness = self.evaluate_fitness(candidate)

            if self.strategy_type == 'comma': # (1, 1)-ES strategy, replace the parent with the offspring                
                x = candidate
                best_fitness = candidate_fitness
            elif self.strategy_type == 'plus': # (1 + 1)-ES strategy, replace the parent with the offspring 
                if candidate_fitness < best_fitness:
                    x = candidate
                    best_fitness = candidate_fitness
        return iterations

def show_results(results, iters=10):
    
    for type in results.keys():
        df  = pd.DataFrame(index = range(iters), columns = results[type].keys())
        for sigma in results[type].keys():
            for i, (iterations) in enumerate(results[type][sigma]):
                df.loc[i, sigma] = iterations

        print(df)
        df.to_csv(f"{type}_results.csv")
        
    

if __name__ == "__main__":
    n = 10 
    max_iterations = 10_000_000
    target = 0.005
    results = {}
    for type in ['plus','comma']:
        results[type] = {}
        for sigma in [0.01, 0.1, 1.0]:
            results[type][sigma] = []
            for i in range(10):
                es = EvolutionStrategy(sigma=sigma, 
                                        strategy_type=type,
                                        max_iterations=max_iterations,
                                        target=target,
                                        n=n)
                iterations = es.run()
                results[type][sigma].append(iterations)
                print(f"{type} ES with sigma={sigma}, run {i + 1}")
                print(f"Iterations: {iterations}")
    
    show_results(results)