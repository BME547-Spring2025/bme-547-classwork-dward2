import pytest

def test_sqrt():
    from my_math_calculator import sqrt
    input_value = -4
    with pytest.raises(ValueError):
        answer = sqrt(-4)