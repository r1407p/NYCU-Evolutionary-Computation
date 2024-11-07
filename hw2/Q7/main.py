import numpy as np
import random
import pandas as pd


class EvolutionStrategy:
    def __init__(self, sigma, strategy_type, max_iterations=10_000_000, target=0.005, n=10, G=1.2, a=0.8, success_threshold=0.2):
        """
        Initialize the parameters for the evolution strategy with the 1/5-rule.
        
        :param sigma: Step-size for Gaussian mutation
        :param strategy_type: Type of evolution strategy ('comma' for (1, 1)-ES, 'plus' for (1 + 1)-ES)
        :param max_iterations: Maximum iterations allowed
        :param target: Target objective function value
        :param n: Dimension of the sphere model
        :param G: Step size increase factor when success rate > 1/5
        :param a: Step size decrease factor when success rate < 1/5
        :param success_threshold: The threshold for success rate (typically 1/5)
        """
        self.sigma = sigma
        self.strategy_type = strategy_type
        self.max_iterations = max_iterations
        self.target = target
        self.n = n
        self.G = G
        self.a = a
        self.success_threshold = success_threshold
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
        success_count = 0  # To track how many offspring improve

        while best_fitness > self.target and iterations < self.max_iterations:
            iterations += 1
            candidate = self.mutate(x)
            parent_fitness = self.evaluate_fitness(x)
            candidate_fitness = self.evaluate_fitness(candidate)

            if self.strategy_type == 'comma':  # (1, 1)-ES strategy, replace the parent with the offspring
                x = candidate
                best_fitness = candidate_fitness
                if candidate_fitness < parent_fitness:
                    success_count += 1
            elif self.strategy_type == 'plus':  # (1 + 1)-ES strategy, replace the parent with the offspring
                if candidate_fitness < best_fitness:
                    x = candidate
                    best_fitness = candidate_fitness
                    if candidate_fitness < parent_fitness:
                        success_count += 1

            # Apply the 1/5-rule: Adjust step size based on success rate
            success_rate = success_count / iterations
            if success_rate > self.success_threshold:
                self.sigma *= self.G  # Increase step size
            else:
                self.sigma *= self.a  # Decrease step size

        return iterations

def show_results(results, iters=10):
    for type in results.keys():
        df = pd.DataFrame(index=range(iters), columns=results[type].keys())
        for sigma in results[type].keys():
            for i, (iterations) in enumerate(results[type][sigma]):
                df.loc[i, sigma] = iterations

        print(df)
        print(df.mean())
        df.to_csv(f"{type}_results.csv")

if __name__ == "__main__":
    n = 10
    max_iterations = 10_000_000
    target = 0.005
    results = {}

    G = 1.2 
    a = 0.8

    for type in ['plus', 'comma']:
        results[type] = {}
        for sigma in [0.01, 0.1, 1.0]:
            results[type][sigma] = []
            for i in range(10):
                es = EvolutionStrategy(sigma=sigma,
                                        strategy_type=type,
                                        max_iterations=max_iterations,
                                        target=target,
                                        n=n,
                                        G=G,
                                        a=a)
                iterations = es.run()
                results[type][sigma].append(iterations)
                print(f"{type} ES with sigma={sigma}, run {i + 1}")
                print(f"Iterations: {iterations}")

    show_results(results)
