# Collatz

Create, plot, and investigate Collatz sequences.

## Collatz Sequences

A Collatz sequence can start from any positive whole number (except 0). The
next term is decided by the following rules:

1. If the previous term is *even*, the next term is half the previous term
2. If the previous term is *odd*, the next term is 3 times the previous term
   plus 1

For example, starting from 12, we get the Collatz sequence:
`12, 6, 3, 10, 5, 16, 8, 4, 2, 1`

The [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)
states that all Collatz sequences will eventually reach 1. This has not been
proven. This module allows you to test the conjecture by making your own Collatz
sequences.

## Demo

To create and plot a Collatz sequence, run a python file containing code like
this:

```python
from collatz import Collatz
# Create a Collatz sequence starting from 77,031 (until it reaches 1)
sequence = Collatz(77031)
# Plot the sequence
sequence.plot()
```

![Line plot of a Collatz sequence starting from 77,031 with linear scale](/img/plot-77031-linear.png)

You can change the scale of the y-axis:

```python
# Plot the sequence with log y-axis scale
sequence.plot(scale='log')
```

![Line plot of a Collatz sequence starting from 77,031 with log scale](/img/plot-77031-log.png)

To compare multiple Collatz sequences on a single plot:

```python
from collatz import Collatz, plot_comparison
sequences = [Collatz(1017), Collatz(1016), Collatz(1015)]
plot_comparison(sequences)
```

![Line plot of three Collatz sequences with linear scale](/img/plot-comparison-3-linear.png)

As above, but using log scale:

```python
from collatz import Collatz, plot_comparison
sequence_1 = Collatz(7579309213675935)
sequence_2 = Collatz(93571393692802302)
plot_comparison([sequence_1, sequence_2], scale='log')
```

![Line plot of two Collatz sequences with log scale](/img/plot-comparison-2-log.png)
