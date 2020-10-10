'''Investigate the Collatz Conjecture.
'''

__version__ = '0.0'
__author = 'Jacob'

class Collatz:
    '''Create a Collatz sequence starting from any whole number > 0.'''
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
        first_term = self._sequence[0]
        length = len(self._sequence)
        return f'Collatz(first_term={first_term:,}, length={length})'

    def __str__(self):
        first_term = self._sequence[0]
        length = len(self._sequence)
        return f'Collatz sequence starting from {first_term:,} with {length} terms'

    def __iter__(self):
        return iter(self._sequence)
    
    def __getitem__(self, item):
        return self._sequence[item]

    def __eq__(self, other):
        if self._sequence == other:
            return True
        return False
    
    def __len__(self):
        return len(self._sequence)