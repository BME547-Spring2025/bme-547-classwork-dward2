import pytest


@pytest.mark.parametrize("test_value, expected", [
    (60, "Normal"),
    (40, "Borderline Low"),
    (20, "Low")
])
def test_analyze_generic_result(test_value, expected):
    # Arrange
    from blood_analysis import analyze_generic_result
    test_ranges = {"Normal": (60, 1000),
                   "Borderline Low": (40, 59),
                   "Low":(0, 39)}
 
    # Act
    answer = analyze_generic_result(test_value,
                                    test_ranges)
    # Assert
    assert answer == expected

    
    
