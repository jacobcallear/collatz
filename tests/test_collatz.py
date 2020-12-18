'''Test Collatz class.'''

import operator

import pytest

from collatz import Collatz
from tests.example_sequences import example_sequences


@pytest.mark.parametrize('example_sequence', example_sequences)
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


@pytest.mark.parametrize('wrong_input_type', [
    'a string',
    None,
    [1],
    (1,),
    {},
    set()
])
def test_raise_type_error(wrong_input_type):
    '''Check TypeError raised when input is not a float or integer.'''
    with pytest.raises(TypeError):
        Collatz(wrong_input_type)


@pytest.mark.parametrize('wrong_input_value', [
    1.1,
    1000.9,
    0,
    -0,
    -1,
    -1.3,
    -1000,
    -1000.5
])
def test_raise_value_error(wrong_input_value):
    '''Check ValueError raised for negative numbers, 0, and non-integer floats.
    '''
    with pytest.raises(ValueError):
        Collatz(wrong_input_value)


@pytest.mark.parametrize('number_1, number_2, ordering', [
    # Collatz(big_num) > Collatz(small_num)
    (3, 2, operator.gt),
    (100, 99, operator.gt),
    (1000, 1, operator.gt),
    # Collatz(small_num < Collatz(big_num))
    (1, 4, operator.lt),
    (149, 150, operator.lt),
    (3, 1000, operator.lt),
    # Collatz(x) == Collatz(x)
    (785, 785, operator.eq),
    (573, 573, operator.le),
    (946, 946, operator.ge),
    # Collatz(x) != Collatz(y)
    (9, 2, operator.ne),
    (930457, 3984570, operator.ne)
])
def test_ordering(number_1, number_2, ordering):
    '''Test comparison ordering as for tuples.'''
    assert ordering(Collatz(number_1), Collatz(number_2))
