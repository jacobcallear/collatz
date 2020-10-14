'''Investigate the Collatz Conjecture.
'''
from functools import total_ordering

__version__ = '0.0'
__author__ = 'Jacob'

@total_ordering
class Collatz:
    '''Create a Collatz sequence starting from any whole number > 0.'''
    # ==============================
    # INTERNAL METHODS
    def __init__(self, start_number):
        if not isinstance(start_number, (int, float)):
            raise TypeError('First term must be a whole number (int or float)')
        if isinstance(start_number, float) and not start_number.is_integer():
            raise ValueError('First term must be a whole number')
        if start_number < 1:
            raise ValueError('First term must be > 0')
        self._sequence = tuple(self._generate_sequence(start_number))
    
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
        if len(self._sequence) < 10:
            abbreviated_sequence = str(self._sequence).strip('()')
        else:
            first_three_terms = sequence_to_string(self._sequence[:3])
            last_five_terms = sequence_to_string(self._sequence[-5:])
            abbreviated_sequence = f'{first_three_terms}, ..., {last_five_terms}'
        return f'{type(self).__name__}([{abbreviated_sequence}])'

    def __str__(self):
        first_term = self.convert_to_scientific_form(self._sequence[0],
                                                     decimal_places=2)
        length = self.convert_to_scientific_form(len(self._sequence),
                                                     decimal_places=2)
        return f'Collatz sequence starting from {first_term} with {length} terms'

    def __iter__(self):
        return iter(self._sequence)
    
    def __getitem__(self, item):
        return self._sequence[item]

    def __eq__(self, other):
        if self._sequence == other:
            return True
        return False

    def __lt__(self, other):
        if self._sequence < other:
            return True
        return False
    
    def __len__(self):
        return len(self._sequence)

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