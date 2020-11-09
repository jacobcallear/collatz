# Collatz

Create, plot, and investigate Collatz sequences.

## Collatz Sequence

A Collatz sequence can start from any positive whole number (except 0). The
next term is decided by the following rules:

1. If the previous term is *even*, the next term is half the previous term
2. If the previous term is *odd*, the next term is 3 times the previous term
   plus 1

For example, starting from 12, we get the Collatz sequence:
`12, 6, 3, 10, 5, 16, 8, 4, 2, 1`

## Collatz Conjecture

The [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)
states that all Collatz sequences will eventually reach 1. This has not been
proven. This module allows you to test the conjecture by making your own Collatz
sequences.

## Demo

To create and plot a Collatz sequence, run a python file containing code like
this:

```python
from collatz import Collatz
sequence = Collatz(77031)
print(sequence)
sequence.plot()
sequence.plot(scale='log')
```

Output:

```
Collatz sequence starting from 77,031 with 351 terms
```

![Plot of a Collatz sequence starting from 77,031 with linear scale](/img/plot-77031-linear.png)

![Plot of a Collatz sequence starting from 77,031 with log scale](/img/plot-77031-log.png)
