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
    from database import find_patient, db
    db.clear()
    new_patient = Patient("First", "Last", 1, 30)
    db.append(new_patient)
    db.append(Patient("Two", "Two", 2, 22))
    # Act
    answer = find_patient(1)
    # Assert
    assert answer == new_patient


def test_add_test_data_to_db():
    # Arrange
    from database import add_test_data_to_db, db
    db.clear()
    db.append(Patient("One", "One", 1, 11))
    db.append(Patient("Two", "Two", 2, 22))
    test_data = ["1,HDL,100\n",
                 "1,LDL,50\n",
                 "2,HDL,75\n"]
    # Act
    add_test_data_to_db(test_data)
    # Assert
    assert len(db[0].tests) == 2
    assert db[0].tests[1][1] == 50
    assert len(db[1].tests) == 1
