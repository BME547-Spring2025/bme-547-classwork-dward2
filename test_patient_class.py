import pytest
from patient_class import Patient
from health_db_server import connect_to_db

# Create connection, and then delete any existing info
connect_to_db()
Patient.collection.drop()


def test_patient_init():
    # Arrange
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


def test_patient_save_new():
     # Arrange
    Patient.clear_database()
    first_name = "Ann"
    last_name = "Ables"
    mrn = 123
    age = 30
    new_patient = Patient(first_name, last_name, mrn, age)
    new_patient.add_test_result("LDL", 50)
    # Act
    new_patient.save()
    # Assert
    found_patient = Patient.get_patient_from_db(mrn)
    assert new_patient == found_patient


def test_patient_save_updated():
    # Arrange
    Patient.clear_database()
    first_name = "Ann"
    last_name = "Ables"
    mrn = 123
    age = 30
    new_patient = Patient(first_name, last_name, mrn, age)
    new_patient.add_test_result("LDL", 50)
    new_patient.save()
    existing_patient = Patient.get_patient_from_db(mrn)
    existing_patient.add_test_result("HDL", 45)
    # Act
    existing_patient.save()
    # Assert
    found_patient = Patient.get_patient_from_db(mrn)
    assert len(found_patient.tests) == 2
    assert found_patient.tests[-1][1] == 45