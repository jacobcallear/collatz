'''Plot multiple sequences.
'''
from matplotlib import pyplot as plt

def plot_comparison(sequences, scale='linear'):
    '''Plot each sequence on the same plot.'''
    linear = True if scale == 'linear' else False
    plt.style.use('ggplot')
    for sequence in sequences:
        if len(sequence) == 1:
            print(f'ERROR: Sequence {sequence!r} only contains one element')
        try:
            plt.plot(range(len(sequence)), sequence)
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
    plt.show()
