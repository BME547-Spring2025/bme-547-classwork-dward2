from health_db_server import app, db

client = app.test_client()


def test_post_new_patient():
    db.clear()
    test_patient = {
        "name": "Patient Zero",
        "id": 123,
        "blood_type": "O+"
    }
    r = client.post("/new_patient",
                    json=test_patient)
    assert r.status_code == 200
    assert r.json["message"] == "Patient added"
    assert len(db) == 1


def test_post_new_patient_bad_key():
    db.clear()
    test_patient = {
        "naaaame": "Patient Zero",
        "id": 123,
        "blood_type": "O+"
    }
    r = client.post("/new_patient",
                    json=test_patient)
    assert r.status_code == 400
    assert r.text == "Key name is not found in input."
    assert len(db) == 0
