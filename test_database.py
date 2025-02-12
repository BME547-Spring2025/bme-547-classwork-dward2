import pytest
from patient_class import Patient


def test_create_patient():
    # Arrange
    from database import create_patient
    input_line = "Ann Ables,1553,30"
    expected = Patient("Ann", "Ables", 1553, 30)
    # Act
    answer = create_patient(input_line)
    # Assert
    assert answer == expected


def test_create_database():
    # Arrange
    from database import create_database, db
    # Arrange
    db.clear()
    input_data = ["Ann Ables,1553,30",
                  "Bob Boyles,1,20"]
    # Act
    create_database(input_data)
    # Assert
    assert len(db) == 2


def test_create_database_other():
    # Arrange
    from database import create_database, db
    db.clear()
    input_data = ["Ann Ables,1553,30",
                  ]
    # Act
    create_database(input_data)
    # Assert
    assert len(db) == 1


def test_find_patient():
    # Arrange
    from database import find_patient, db, create_database
    db.clear()
    new_patient = Patient("First", "Last", 1, 30)
    db.append(new_patient)
    db.append(Patient("Two", "Two", 2, 22))
    # Act
    answer = find_patient(1)
    # Assert
    assert answer == new_patient


@pytest.mark.parametrize("age, expected", [
    (15, True),
    (22, False)])
def test_patient_is_minor_true(age, expected):
    # Arrange
    patient = Patient("First", "Last", 1, age)
    # Act
    answer = patient.is_minor()
    # Assert
    assert answer == expected


def test_patient_add_test_result():
    # Arrange
    patient = Patient("First", "Last", 1, 15)
    test_name = "HDL"
    test_value = 50
    # Act
    patient.add_test_result(test_name, test_value)
    # Assert
    assert patient.tests[-1] == (test_name, test_value)
