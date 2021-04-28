'''Plot multiple sequences.
'''
from matplotlib import pyplot as plt

from collatz import Collatz

def plot_comparison(sequences, scale='linear'):
    '''Plot each sequence in sequences on the same plot.'''
    linear = scale == 'linear'
    plt.style.use('ggplot')
    plotted_sequences = 0
    for sequence in sequences:
        if len(sequence) == 1:
            print(f'Sequence {sequence!r} not plotted as only contains one element')
            continue
        x_values = range(len(sequence))
        sequence_label = Collatz.convert_to_scientific_form(sequence[0])
        try:
            plt.plot(x_values, sequence, label=sequence_label)
            plotted_sequences += 1
        except OverflowError:
            print(f'ERROR: Sequence {sequence!r} too large to plot')
            continue
    # Axis limits
    plt.xlim(0)
    y_min = 0 if linear else 1
    plt.ylim(y_min)
    # Labels
    plt.title(f'Comparison plot of {plotted_sequences} Collatz sequences')
    plt.xlabel('Step')
    plt.ylabel(fr'Value - $\it{{{scale}\ scale}}$')
    # Scale
    scale = 'linear' if linear else 'log'
    plt.yscale(scale)
    if len(sequences) <= 10:
        plt.legend(title='First term', facecolor='#fdf6e3', framealpha=1)
    plt.show()
