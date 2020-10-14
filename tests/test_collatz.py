'''Test Collatz class.'''
import pytest

from collatz import Collatz

@pytest.fixture
def example_sequence():
    return (
    27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121,
    364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175,
    526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502,
    251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438,
    719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367,
    4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300,
    650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80,
    40, 20, 10, 5, 16, 8, 4, 2, 1
)

@pytest.fixture
def example_collatz_class():
    return Collatz(27)

def test_setup(example_sequence, example_collatz_class):
    '''Check that example sequence and collatz class are comparable'''
    assert example_sequence[0] == example_collatz_class[0]

def test_sequence(example_sequence, example_collatz_class):
    '''Check Collatz sequence generated correctly.'''
    assert example_sequence == example_collatz_class

def test_convert_to_scientific_form():
    '''Test method converts to scientific form.'''
    # Test imprecise scientific form
    number = 852074902357402935742905784029357842930574
    expected_output = '~8.520749 x 10^41'
    actual_output = Collatz.convert_to_scientific_form(
        number,
        decimal_places=6,
        threshold=0)
    assert expected_output == actual_output
    # Test precise scientific form
    number = 48237490000000000000000000000000000000000000000000
    expected_output = '4.823749 x 10^49'
    actual_output = Collatz.convert_to_scientific_form(
        number,
        decimal_places=6,
        threshold=0)
    assert expected_output == actual_output
    # Test comma separators
    number = 287540938670578023578420935784209357842903578420935784
    expected_output = f'{number:,}'
    actual_output = Collatz.convert_to_scientific_form(number, threshold=None)
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
