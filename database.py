"""
Patient = [last name, first name, mrn (int), age(int),
            [(test_name(str), test_value(int)),
              (test_name(str), test_value(int))]]

* Read in test results from file
* for each test result, add the ("HDL", 45) tuple to the
correct patient
* print out db to see if it worked


"""


db = []


def load_patient_data_file(filename):
    in_file = open(filename, 'r')
    data = in_file.readlines()
    in_file.close()
    return data


def load_patient_data_file_singles(filename):
    with open(filename, 'r') as in_file:
        data = []
        headers = in_file.readline()
        for line in in_file:
            data.append(line)
    return data


def create_database(data):
    for line in data:
        patient = create_patient(line)
        db.append(patient)


def create_patient(line):
    line = line.strip("\n")
    data = line.split(",")
    first_name, last_name = data[0].split(" ")
    mrn = int(data[1])
    age = int(data[2])
    patient = [last_name, first_name, mrn, age, []]
    return patient


def find_patient(mrn):
    for patient in db:
        if patient[2] == mrn:
            return patient
    return None


def add_test_result_to_patient(patient, test_name,
                               test_value):
    new_result = (test_name, test_value)
    patient[4].append(new_result)


def add_test_data_to_db(test_data):
    for data in test_data:
        line = data.strip("\n")
        mrn, test_name, test_value = line.split(",")
        mrn = int(mrn)
        patient = find_patient(mrn)
        add_test_result_to_patient(patient, test_name,
                                   int(test_value))


def main():
    data = load_patient_data_file("patient_data.txt")
    create_database(data)
    print(db)
    test_data = load_patient_data_file(
        "blood_test_data.txt")
    add_test_data_to_db(test_data)
    print(db)


if __name__ == "__main__":
    main()
