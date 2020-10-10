'''Investigate the Collatz Conjecture.
'''

__version__ = '0.0'
__author = 'Jacob'

class Collatz:
    '''Create a Collatz sequence starting from any whole number.'''
    def __init__(self, start_number):
        self.sequence = tuple(self._generate_sequence(start_number))
    
    @staticmethod
    def _generate_sequence(num):
        yield num
        while num != 1:
            if num % 2:
                num = 3*num + 1
            else:
                num //= 2
            yield num

    def __repr__(self):
        first_term = self.sequence[0]
        length = len(self.sequence)
        return f'Collatz(first_term={first_term:,}, length={length})'

    def __str__(self):
        first_term = self.sequence[0]
        length = len(self.sequence)
        return f'Collatz sequence starting from {first_term:,} with {length} terms'