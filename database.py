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
    patient = {"Last Name": last_name,
               "First Name": first_name,
               "MRN": mrn,
               "Age": age,
               "Tests": []}
    return patient


def find_patient(mrn):
    for patient in db:
        if patient["MRN"] == mrn:
            return patient
    return None


def add_test_result_to_patient(patient, test_name,
                               test_value):
    new_result = (test_name, test_value)
    patient["Tests"].append(new_result)


def add_test_data_to_db(test_data):
    for data in test_data:
        line = data.strip("\n")
        mrn, test_name, test_value = line.split(",")
        mrn = int(mrn)
        patient = find_patient(mrn)
        add_test_result_to_patient(patient, test_name,
                                   int(test_value))


def is_minor(patient):
    if patient["Age"] < 18:
        return True
    else:
        return False


def create_patient_output(patient):
    out_string = ""
    out_string += "Name: {} {}\n".format(patient["First Name"],
                                         patient["Last Name"])
    out_string += "MRN: {}\n".format(patient["MRN"])
    if is_minor(patient):
        status = "Minor"
    else:
        status = "Adult"
    out_string += "Status: {}\n".format(status)
    out_string += "Test Results: {}\n".format(patient["Tests"])
    return out_string


def output_database():
    for patient in db:
        out_string = create_patient_output(patient)
        print(out_string)


def main():
    data = load_patient_data_file("patient_data.txt")
    create_database(data)
    output_database()
    test_data = load_patient_data_file(
        "blood_test_data.txt")
    add_test_data_to_db(test_data)
    output_database()


def class_demo():
    patient_1 = Patient()
    patient_1.first_name = "David"
    patient_2 = Patient()
    patient_2.first_name = "John"
    print(patient_1.first_name, patient_2.first_name)


if __name__ == "__main__":
    class_demo()
    # main()
