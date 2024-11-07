## Observe the running processes of problem 3
### problem
Compare and contrast the results you obtained in problem 3 and discuss what you think about the difference between (1 1)-ES and (1+1)-ES.

## step size \( \sigma \)
- **(1,1)-ES Results**:
  - Across all values of \( \sigma \), the (1,1)-ES method consistently reached the maximum number of iterations (10,000,000) without meeting the objective threshold of 0.005.
  - The lack of improvement regardless of step size suggests that this strategy lacks an efficient selection mechanism to focus on better solutions.
  
- **(1+1)-ES Results**:
  - The (1+1)-ES strategy demonstrated variability in results based on the step size:
    - For **\( \sigma = 0.01 \)** and **\( \sigma = 0.1 \)**, the strategy converged in fewer generations, with average generation counts of 823.8 and 218,660.8, respectively.
    - With **\( \sigma = 1.0 \)**, however, the (1+1)-ES also reached the maximum number of iterations, indicating excessive variance and ineffective convergence with large mutation sizes.

### Strategy Type
- **(1,1)-ES**:
  - This strategy replaces the parent with the offspring regardless of fitness improvement, leading to a more exploratory search that lacks focus on fitter regions. Consequently, it behaves as a random walk, often failing to converge in constrained runs.
  
- **(1+1)-ES**:
  - The (1+1)-ES employs a selective replacement mechanism, where the offspring replaces the parent only if it has a better fitness. This selection pressure allows the algorithm to refine the solution around promising areas and promotes faster convergence.
  - The strategy is more effective in balancing exploration and exploitation, particularly with smaller \( \sigma \) values, where controlled mutations lead to finer adjustments.

### Summary of Observations
- **Efficiency of Selective Replacement**: The (1+1)-ES’s selective replacement allows it to maintain beneficial traits and converge more effectively, especially at smaller \( \sigma \) values. In contrast, the (1,1)-ES’s random replacement hinders convergence.
- **Influence of Step Size**
- **Influence of Step Size**: Smaller step sizes (e.g., \( \sigma = 0.01 \)) enhance the (1+1)-ES's ability to refine solutions, while larger steps increase the risk of excessive divergence in both strategies.
  
In conclusion, the (1+1)-ES provides a more efficient approach for correlated Gaussian mutation optimization, as its selective mechanism enables it to focus on fit individuals, whereas the (1,1)-ES is less suited for tasks requiring rapid convergence due to its lack of selection pressure.