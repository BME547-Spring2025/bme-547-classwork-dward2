from health_db_server import app, connect_to_db
from patient_class import Patient

client = app.test_client()
connect_to_db()


def test_post_new_patient():
    Patient.clear_database()
    test_patient = {
        "name": "Patient Zero",
        "id": 123,
        "blood_type": "O+"
    }
    r = client.post("/new_patient",
                    json=test_patient)
    assert r.status_code == 200
    assert r.json["message"] == "Patient added"
    added_patient = Patient.get_patient_from_db(123)
    assert added_patient.blood_type == "O+"


def test_post_new_patient_bad_key():
    Patient.clear_database()
    test_patient = {
        "naaaame": "Patient Zero",
        "id": 123,
        "blood_type": "O+"
    }
    r = client.post("/new_patient",
                    json=test_patient)
    assert r.status_code == 400
    assert r.text == "Key name is not found in input."
    added_patient = Patient.get_patient_from_db(123)
    assert added_patient is None


def test_post_add_test():
    # Arrange
    Patient.clear_database()
    test_patient = Patient("Patient",
                           "Zero",
                           234)
    test_patient.add_test_result("LDL", 40)
    test_patient.save()
    new_test_json = {"id": 234,
                     "test_name": "HDL",
                     "test_result": 50}
    # Act
    r = client.post("/add_test",
                    json=new_test_json)
    assert r.status_code == 200
    assert r.text == "Test added"
    found_patient = Patient.get_patient_from_db(234)
    assert len(found_patient.tests) == 2
    assert found_patient.tests[-1][1] == 50
