## Comparison of (1,1)-ES and (1+1)-ES Results with Different Mutation Strategies

### Summary of Observations
1. **Correlated Gaussian Mutation**:
   - For **(1,1)-ES**, none of the tests converged within the limit of 10 million iterations, regardless of the mutation rate (\(\sigma\)). This suggests that the mutation strategy struggled to effectively find solutions.
   - With **(1+1)-ES**, results varied: small mutation rates (like \(\sigma = 0.01\) and \(\sigma = 0.1\)) generally allowed faster convergence, while the largest rate (\(\sigma = 1.0\)) didn't help the algorithm reach a solution in most cases.

2. **Uncorrelated Gaussian Mutation**:
   - **(1,1)-ES** showed similar issues to correlated mutation, with all runs maxing out at 10 million iterations and no successful convergence.
   - **(1+1)-ES**, however, performed much better. The majority of tests converged well before reaching 10 million iterations, especially with smaller mutation rates (\(\sigma = 0.01\) and \(\sigma = 0.1\)). The larger mutation rate (\(\sigma = 1.0\)) had more mixed outcomes but still showed some promise.

3. **1/5-Rule with Gaussian Mutation**:
   - Again, **(1,1)-ES** couldn’t reach a solution within 10 million iterations.
   - For **(1+1)-ES**, though, applying the 1/5-rule led to a noticeable improvement. The algorithm converged significantly faster with all mutation rates, reducing the average number of iterations needed to find solutions compared to the previous methods.

### Key Takeaways and Comparisons
- **Why the 1/5-Rule Helped**: The 1/5-rule works by adjusting the mutation step size (how far solutions can "jump" in each step) based on the algorithm’s success rate. If progress slows down, the step size increases to help explore the search space more. When near a solution, it decreases to fine-tune the final steps. This adaptability was a clear advantage, especially with higher mutation rates that previously struggled to converge.

- **Comparing Mutation Strategies**:
   - The **(1+1)-ES approach** consistently outperformed (1,1)-ES because it’s designed to keep the best solution at each step, making it more likely to progress steadily toward a solution.
   - **Correlated vs. Uncorrelated Mutation**: Uncorrelated mutation, where each dimension can change independently, was more effective than correlated mutation. This freedom helps the algorithm better navigate the search space.
   - **1/5-Rule’s Advantage**: By allowing self-adjustment, the 1/5-rule enabled the algorithm to better balance exploring new solutions with focusing on promising ones. It excelled particularly in cases where static mutation rates led to either slow progress or overshooting a solution.

### **onclusion**
The 1/5-rule is a powerful tool for self-adjusting mutation rates based on how successful the algorithm is at each step. By adapting to the problem dynamically, it can effectively guide the search process. This strategy proved especially useful for challenging or noisy problems, where other methods couldn’t converge within the maximum allowed steps. The 1/5-rule’s success here highlights its value in making mutation strategies more robust and adaptable.
