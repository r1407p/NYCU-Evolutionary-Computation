## feature frequency
### Problem
Given:
- A population of \( \mu \) individuals, each represented as a bit-string of length \( L \).
- Let the frequency of allele 1 be 0.25 at position i, that is, 25% of all individuals contains a 1, and 75% a 0 at the ith position on the chromosome. 

Determine how the allele frequency changes after performing \( k \) crossover operations with:
1. One-point crossover.
2. Uniform crossover.


### One-Point Crossover
In one-point crossover, a random crossover point is selected, and the segments to the right of that point in two parent bit-strings are swapped.

However, after a crossover the allele frequency at position \( i \) will remain at 0.25, since the origin of both is 0.25.
So after k crossover the allele frequency at position \( i \) will remain at 0.25

### Uniform Crossover
In uniform crossover, each gene (bit) position is independently swapped between the two parents with a certain probability (often 0.5).

However, after a crossover the allele frequency at position \( i \) will remain at 0.25, since the origin of both is 0.25.
So after k crossover the allele frequency at position \( i \) will remain at 0.25

### Summary
For both one-point and uniform crossover, the allele frequency at position \( i \) will remain at 0.25 after \( k \) crossovers. This is because crossover operations are recombination techniques that do not inherently change allele frequencies; they only rearrange the genetic material among individuals in the population.