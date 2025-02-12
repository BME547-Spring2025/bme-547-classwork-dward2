import pytest


def test_patient_init():
    # Arrange
    from patient_class import Patient
    first_name = "Ann"
    last_name = "Ables"
    mrn = 123
    age = 30
    # Act
    answer = Patient(first_name, last_name, mrn, age)
    # Assert
    assert answer.first_name == first_name
    assert answer.last_name == last_name
    assert answer.mrn == mrn
    assert answer.age == age
    assert answer.tests == []


@pytest.mark.parametrize("age, expected", [
    (15, True),
    (22, False)])
def test_patient_is_minor(age, expected):
    # Arrange
    from patient_class import Patient
    patient = Patient("First", "Last", 1, age)
    # Act
    answer = patient.is_minor()
    # Assert
    assert answer == expected


def test_patient_add_test_result():
    # Arrange
    from patient_class import Patient
    patient = Patient("First", "Last", 1, 15)
    test_name = "HDL"
    test_value = 50
    # Act
    patient.add_test_result(test_name, test_value)
    # Assert
    assert patient.tests[-1] == (test_name, test_value)
