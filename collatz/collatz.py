'''Investigate the Collatz Conjecture.
'''
from matplotlib import pyplot as plt

__version__ = '0.0'
__author__ = 'Jacob'


class Collatz(tuple):
    '''Create a Collatz sequence starting from any whole number > 0.'''
    # ==============================
    # INTERNAL METHODS
    def __new__(cls, start_number):
        cls._check_valid_first_term(start_number)
        sequence = cls._generate_sequence(start_number)
        return super().__new__(cls, sequence)

    @staticmethod
    def _check_valid_first_term(num):
        '''Raise error if given start number is an invalid type or value.'''
        if not isinstance(num, (int, float)):
            raise TypeError('First term must be a whole number (int or float)')
        if isinstance(num, float) and not num.is_integer():
            raise ValueError('First term must be a whole number')
        if num < 1:
            raise ValueError('First term must be > 0')

    @staticmethod
    def _generate_sequence(num):
        num = int(num)
        yield num
        while num != 1:
            if num % 2:
                num = 3*num + 1
            else:
                num //= 2
            yield num

    def __repr__(self):
        '''Returns numpy.array style repr.'''
        def sequence_to_string(sequence):
            scientific_form_sequence = (
                self.convert_to_scientific_form(term, decimal_places=3, threshold=10)
                for term in sequence
            )
            return ', '.join(scientific_form_sequence)
        # ----------
        if len(self) < 10:
            abbreviated_sequence = str(tuple(self)).strip('()')
        else:
            first_three_terms = sequence_to_string(self[:3])
            last_five_terms = sequence_to_string(self[-5:])
            abbreviated_sequence = f'{first_three_terms}, ..., {last_five_terms}'
        return f'{type(self).__name__}([{abbreviated_sequence}])'

    def __str__(self):
        first_term = self.convert_to_scientific_form(self[0], decimal_places=2)
        length = self.convert_to_scientific_form(len(self), decimal_places=2)
        return f'Collatz sequence starting from {first_term} with {length} terms'

    # ==============================
    def plot(self, scale='linear'):
        '''Plot sequence.

        Args:
            scale (str): If 'linear', uses linear y-axis scale; if 'log' uses
                log scale.
        '''
        linear = scale == 'linear'
        colour = 'g' if linear else 'r'
        plt.style.use('ggplot')
        try:
            plt.plot(self, colour)
        except OverflowError:
            print('ERROR: Sequence too large to plot')
            return
        # Axis limits
        plt.xlim(0)
        y_min = 0 if linear else 1
        plt.ylim(y_min)
        # Labels
        first_term = self.convert_to_scientific_form(self[0], threshold=11, decimal_places=3)
        plt.title(f'Collatz sequence starting from {first_term}')
        plt.xlabel('Step')
        plt.ylabel(fr'Value - $\it{{{scale}\ scale}}$')
        # Scale
        scale = 'linear' if linear else 'log'
        plt.yscale(scale)
        plt.show()

    # ==============================
    @staticmethod
    def convert_to_scientific_form(number, decimal_places=6, threshold=10):
        '''Convert a positive integer to scientific form or add comma separators.

        Doesn't raise OverflowError for large numbers, unlike f'{:e}'

        Args:
            number (int): Number to format
            decimal_places (int): Number of decimal places for scientific form.
                Must be < 15.
            threshold (int): Numbers with more digits than the threshold are
                converted to scientific form. Otherwise, commas separators are
                added.
        '''
        if decimal_places > 14:
            raise ValueError('Maximum precision 14 decimal places')
        if threshold is None or len(str(number)) <= threshold:
            return f'{number:,}'
        # If all digits after decimal point == 0, set precision to exact
        if all(ch == '0' for ch in str(number)[decimal_places+1:]):
            precision = ''
        else:
            precision = '~'
        exponent = len(str(number)) - 1
        coefficient = f'{number / 10**exponent:.{decimal_places}f}'
        # If rounding resulted in a coefficient of 10...
        if coefficient.startswith('10.'):
            coefficient = coefficient.replace('10.', '1.', 1)
            exponent += 1
        return f'{precision}{coefficient} x 10^{exponent}'
