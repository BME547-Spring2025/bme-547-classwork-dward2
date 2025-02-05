from database import db


def test_create_patient():
    from database import create_patient
    input_line = "Ann Ables,1553,30"
    expected = ["Ables", "Ann", 1553, 30, []]
    answer = create_patient(input_line)
    assert answer == expected


def test_create_database():
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
    from database import create_database, db
    db.clear()
    input_data = ["Ann Ables,1553,30",
                  ]
    create_database(input_data)
    assert len(db) == 1
    
    
def test_find_patient():
    from database import find_patient, db, create_database
    db.clear()
    db.append(["Last", "First", 1, 30,[]])
    answer = find_patient(1)
    assert answer[0] == "Last"
    