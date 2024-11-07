## Compare and contrast the results you obtained in problems 3 and 5.
Discuss what you think about the self-adaptation.

### (1, 1)-ES with Correlated vs. Uncorrelated Mutation:
- Both **correlated** and **uncorrelated Gaussian mutations** failed to converge on the target within the maximum number of iterations (10 million) across all step sizes for (1, 1)-ES. This suggests that neither mutation type provided sufficient adaptation to reach the goal with this strategy.
- The lack of adaptability in (1, 1)-ES reflects the high dependency on initial conditions and the step-size chosen. Without self-adaptive mechanisms, the strategy is unable to explore the solution space effectively and converge to the target.

### (1 + 1)-ES with Correlated Mutation:
- For **correlated mutation** with (1 + 1)-ES, there was a notable dependency on the step size. Specifically, lower step sizes (σ = 0.01 and 0.1) performed much better, with the average iterations being significantly less than for σ = 1.0.
- However, the correlated mutation method with a high step size (σ = 1.0) also failed to converge within the set limit, indicating that the mutation step-size adjustment may not have been sufficient to facilitate convergence for larger initial step sizes.

### (1 + 1)-ES with Uncorrelated Mutation:
- **Uncorrelated Gaussian mutation** with self-adaptive step sizes in the (1 + 1)-ES strategy shows substantial improvement over correlated mutation, particularly with smaller and moderate step sizes.
- This self-adaptive mechanism resulted in faster convergence across runs, showing average iterations that are substantially lower than those seen in correlated mutation results for both low and moderate step sizes.
- For the larger step size (σ = 1.0), the uncorrelated mutation still showed an improvement, though performance degraded slightly compared to smaller step sizes.

### Self-Adaptation:
- **Self-adaptation** in uncorrelated Gaussian mutation helped the (1 + 1)-ES strategy adapt its mutation steps dynamically, allowing it to "fine-tune" the step-size based on the fitness landscape. This adjustment likely prevents large step sizes from overshooting and allows smaller step sizes to explore efficiently around potential minima.
- In contrast, the lack of effective self-adaptation in correlated mutations made it difficult to find an optimal balance between exploration and exploitation. This highlights the value of self-adaptation, especially in complex landscapes or higher-dimensional optimization problems, where an initial, fixed step size may not be suitable for the entire search process.
- Overall, **self-adaptive mechanisms enable the algorithm to adjust its mutation strengths based on progress, thereby achieving a balance between fast convergence and the ability to escape local optima**. This flexibility is particularly advantageous in (1 + 1)-ES, where it can guide the search more effectively than a rigid approach seen in the (1, 1)-ES results.

### Parameters:
- **n = 10**: The dimension of the optimization problem, which determines the size of the individual solution vector.
- **max_iterations = 10,000,000**: The maximum number of iterations allowed for the optimization algorithm to converge to the target solution.
- **target = 0.005**: The target objective function value (f(x)) that the algorithm is trying to reach.
- **τ (tau) = 1 / np.sqrt(2 * np.sqrt(n))**: This parameter controls the step size adaptation and is used to adjust the step size during the evolution process. It is set based on the problem's dimensionality and helps maintain diversity in the population.
- **τ' (tau_prime) = 1 / np.sqrt(2 * n)**: This parameter is used for adaptive mutation step sizes. It also scales the step size with respect to the problem's dimensionality, but it focuses on the global scaling of mutation.
- **ε₀ (epsilon) = 1e-6**: A small value used for mutation scaling or convergence criteria. This ensures numerical stability and prevents the step size from becoming too small, allowing the algorithm to continue progressing without stagnation.