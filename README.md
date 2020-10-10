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
>>> c = Collatz(10**999 - 1)
>>> c
Collatz(first_term=~1.000000 * 10^999, length=31713)
>>> c[-1]
1
>>> Collatz.convert_to_scientific_form(c[0])
'~1.000000 * 10**999'
```