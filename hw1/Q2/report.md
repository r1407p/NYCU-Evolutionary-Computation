To achieve precision 0.001 in the interval [0, 1].

We need at least (1-0)/0.001 = 1000 distinct values.

```
--> 2^x >= 1000
--> x >= log2(1000)
--> x >= 9.97
--> x need to greater or equal 10
```

we need at least 10 bits to represent the value with a precision of 0.001