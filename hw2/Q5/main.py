import numpy as np
import random
import pandas as pd

class EvolutionStrategyUncorrelated:
    def __init__(self, sigma, strategy_type, max_iterations=10_000_000, target=0.005, n=10, tau=0.1, tau_prime=0.1, epsilon=1e-8):
        """
        Initialize the parameters for the evolution strategy with uncorrelated Gaussian mutation.
        
        :param sigma: Initial step-sizes for Gaussian mutation (can be a scalar or array)
        :param strategy_type: Type of evolution strategy ('comma' for (1, 1)-ES, 'plus' for (1 + 1)-ES)
        :param max_iterations: Maximum iterations allowed
        :param target: Target objective function value
        :param n: Dimension of the sphere model
        :param tau: Learning rate for step-size mutation (dependent on dimension)
        :param tau_prime: Global learning rate for step-size mutation
        :param epsilon: Minimum threshold to avoid too small step sizes
        """
        self.sigma = np.full(n, sigma) 
        self.strategy_type = strategy_type
        self.max_iterations = max_iterations
        self.target = target
        self.n = n
        self.tau = tau
        self.tau_prime = tau_prime
        self.epsilon = epsilon
        self.initial_solution = np.ones(n)  # Starting point (1, 1, ..., 1)

    def evaluate_fitness(self, x):
        """Sphere function: f(x) = sum(x_i^2)"""
        return np.sum(x ** 2)

    def mutate(self, x):
        """Apply uncorrelated Gaussian mutation with n individual step sizes."""
        global_mutation = random.gauss(0, 1) * self.tau_prime
        local_mutation = np.array([random.gauss(0, 1) * self.tau for _ in range(self.n)])

        # Update each step size with the mutation rule
        new_sigma = self.sigma * np.exp(global_mutation + local_mutation)
        new_sigma = np.maximum(new_sigma, self.epsilon)  # Prevent step sizes from becoming too small

        # Mutate each component with its own step size
        offspring = x + np.array([random.gauss(0, s) for s in new_sigma])
        return offspring, new_sigma
        
    def run(self):
        """Run the evolution strategy with uncorrelated mutation and return the number of iterations to meet the target."""
        x = self.initial_solution
        best_fitness = self.evaluate_fitness(x)
        iterations = 0

        while best_fitness > self.target and iterations < self.max_iterations:
            iterations += 1
            candidate, candidate_sigma = self.mutate(x)
            parent_fitness = self.evaluate_fitness(x)
            candidate_fitness = self.evaluate_fitness(candidate)

            if self.strategy_type == 'comma':  # (1, 1)-ES strategy
                x = candidate
                self.sigma = candidate_sigma
                best_fitness = candidate_fitness
            elif self.strategy_type == 'plus':  # (1 + 1)-ES strategy
                if candidate_fitness < best_fitness:
                    x = candidate
                    self.sigma = candidate_sigma
                    best_fitness = candidate_fitness
        return iterations

def show_results(results, iters=10):
    """Display results in a tabular format and save as CSV files."""
    for type in results.keys():
        df  = pd.DataFrame(index = range(iters), columns = results[type].keys())
        for sigma in results[type].keys():
            for i, (iterations) in enumerate(results[type][sigma]):
                df.loc[i, sigma] = iterations

        print(df)
        print(df.mean())
        df.to_csv(f"{type}_results_uncorrelated.csv")

if __name__ == "__main__":
    n = 10
    max_iterations = 10_000_000
    target = 0.005
    tau = 1 / np.sqrt(2 * np.sqrt(n))
    tau_prime = 1 / np.sqrt(2 * n)
    epsilon = 1e-6

    results = {}
    for type in ['plus', 'comma']:
        results[type] = {}
        for sigma in [0.01, 0.1, 1.0]:
            results[type][sigma] = []
            for i in range(10):
                es = EvolutionStrategyUncorrelated(sigma=sigma,
                                                   strategy_type=type,
                                                   max_iterations=max_iterations,
                                                   target=target,
                                                   n=n,
                                                   tau=tau,
                                                   tau_prime=tau_prime,
                                                   epsilon=epsilon)
                iterations = es.run()
                results[type][sigma].append(iterations)
                print(f"{type} ES with uncorrelated sigma={sigma}, run {i + 1}")
                print(f"Iterations: {iterations}")

    show_results(results)
