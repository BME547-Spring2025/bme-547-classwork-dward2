from patient_class import Patient

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
    patient = Patient(first_name, last_name, mrn, age)
    return patient


def find_patient(mrn):
    for patient in db:
        if patient.mrn == mrn:
            return patient
    return None


def add_test_data_to_db(test_data):
    for data in test_data:
        line = data.strip("\n")
        mrn, test_name, test_value = line.split(",")
        mrn = int(mrn)
        patient = find_patient(mrn)
        patient.add_test_result(test_name,
                                int(test_value))


def output_database():
    for patient in db:
        out_string = patient.create_output()
        print(out_string)


def main():
    data = load_patient_data_file("patient_data.txt")
    create_database(data)
    output_database()
    test_data = load_patient_data_file(
        "blood_test_data.txt")
    add_test_data_to_db(test_data)
    output_database()


if __name__ == "__main__":
    main()
