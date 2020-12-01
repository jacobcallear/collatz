'''Test Collatz class.'''
import pytest

from collatz import Collatz
from tests.example_sequences import (
    example_sequence_1, example_sequence_2, example_sequence_3,
    example_sequence_4, example_sequence_5, example_sequence_6,
    example_sequence_7, example_sequence_8, example_sequence_9,
    example_sequence_10, example_sequence_27, example_sequence_97,
    example_sequence_77031, example_sequence_1048576
)

@pytest.mark.parametrize('example_sequence', [
    example_sequence_1, example_sequence_2, example_sequence_3,
    example_sequence_4, example_sequence_5, example_sequence_6,
    example_sequence_7, example_sequence_8, example_sequence_9,
    example_sequence_10, example_sequence_27, example_sequence_97,
    example_sequence_77031, example_sequence_1048576
])
def test_generate_sequences(example_sequence):
    '''Test generated collatz sequences are correct for a few first terms.'''
    first_term = example_sequence[0]
    assert Collatz(first_term) == example_sequence

@pytest.mark.parametrize('input_number, decimal_places, threshold, expected_output', [
    (852074902357402935742905784029357842930574, 6, 0, '~8.520749 x 10^41'),
    (48237490000000000000000000000000000000000000000000, 6, 0, '4.823749 x 10^49'),
    (287540938670578023578420935784209357842903578420935784, 0, None,
     '287,540,938,670,578,023,578,420,935,784,209,357,842,903,578,420,935,784')
])
def test_convert_to_scientific_form(input_number, decimal_places, threshold,
                                    expected_output):
    '''Test method converts to scientific form.'''
    # Act, assert
    actual_output = Collatz.convert_to_scientific_form(
        input_number,
        decimal_places=decimal_places,
        threshold=threshold)
    assert expected_output == actual_output

def test_error_raising():
    '''Check Errors are raised when first term is not an integer > 0.'''
    for wrong_input_type in ('string', None, [1], (1,), {}):
        with pytest.raises(TypeError):
            Collatz(wrong_input_type)
    with pytest.raises(ValueError):
        Collatz(1.1)
    with pytest.raises(ValueError):
        Collatz(0)
        Collatz(-1)

def test_ordering():
    '''Test comparison ordering as for tuples.'''
    assert Collatz(3) > Collatz(2) > Collatz(1)
    assert Collatz(3) >= Collatz(2) >= Collatz(1)
    assert Collatz(10) < Collatz(100) < Collatz(1000)
    assert Collatz(10) <= Collatz(100) <= Collatz(1000)
    assert Collatz(178) == Collatz(178) != Collatz(177)
    assert Collatz(203) >= Collatz(203) <= Collatz(203)
