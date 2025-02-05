def test_create_patient():
    # Arrange
    from database import create_patient
    input_line = "Ann Ables,1553,30"
    expected = {"Last Name": "Ables",
                "First Name": "Ann",
                "MRN": 1553,
                "Age": 30,
                "Tests": []}
    # Act
    answer = create_patient(input_line)
    # Assert
    assert answer == expected


def test_create_database():
    # Arrange
    from database import create_database, db
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
    new_patient = {"Last Name": "Last",
                   "First Name": "First",
                   "MRN": 1,
                   "Age": 30,
                   "Tests": []}
    db.append(new_patient)
    # Act
    answer = find_patient(1)
    # Assert
    assert answer == new_patient
