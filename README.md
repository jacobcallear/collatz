# Collatz

Create, plot, and investigate Collatz sequences.

## Collatz Conjecture

The Collatz sequence is a sequence that meets the following rules:

1. The first term is any non-zero integer
2. If the previous term is *even*, the next term is half the previous term
3. If the previous term is *odd*, the next term is 3 times the previous term
   plus 1

For example, starting with *n = 12*, we get the Collatz sequence:
`12, 6, 3, 10, 5, 16, 8, 4, 2, 1`

The [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)
states that for any starting value, the Collatz sequence will always reach *1*.
This module allows you to test this conjecture.

## Use

```python
>>> from collatz import Collatz
>>> collatz_sequence = Collatz(100)
>>> collatz_sequence
Collatz([100, 50, 25, ..., 16, 8, 4, 2, 1])
>>> print(collatz_sequence)
Collatz sequence starting from 100 with 26 terms
>>> last_five_terms = collatz_sequence[-5:]
>>> last_five_terms
(16, 8, 4, 2, 1)
>>> list(collatz_sequence)
[100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20,
 10, 5, 16, 8, 4, 2, 1]
```