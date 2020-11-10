'''Plot multiple sequences.
'''
from matplotlib import pyplot as plt

from collatz import Collatz

def plot_comparison(sequences, scale='linear'):
    '''Plot each sequence in sequences on the same plot.'''
    linear = True if scale == 'linear' else False
    plt.style.use('ggplot')
    for sequence in sequences:
        if len(sequence) == 1:
            print(f'ERROR: Sequence {sequence!r} only contains one element')
        x_values = range(len(sequence))
        sequence_label = Collatz.convert_to_scientific_form(sequence[0])
        try:
            plt.plot(x_values, sequence, label=sequence_label)
        except OverflowError:
            print(f'ERROR: Sequence {sequence!r} too large to plot')
            continue
    # Axis limits
    plt.xlim(0)
    y_min = 0 if linear else 1
    plt.ylim(y_min)
    # Labels
    plt.title(f'Comparison plot of {len(sequences)} Collatz sequences')
    plt.xlabel('Step')
    plt.ylabel(fr'Value - $\it{{{scale}\ scale}}$')
    # Scale
    scale = 'linear' if linear else 'log'
    plt.yscale(scale)
    if len(sequences) <= 10:
        plt.legend(title='First term', facecolor='#fdf6e3', framealpha=1)
    plt.show()
