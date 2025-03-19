class Patient:

    client = None
    database = None
    collection = None

    def __init__(self, first_name, last_name,
                 mrn, age=0, tests=None, blood_type=None):
        self.first_name = first_name
        self.last_name = last_name
        self.mrn = mrn
        self.age = age
        if tests is None:
            self.tests = []
        else:
            self.tests = tests
        self.blood_type = blood_type

    def __repr__(self):
        return "Patient, mrn={}, {} {}".format(self.mrn,
                                               self.first_name,
                                               self.last_name)

    def __eq__(self, other):
        if isinstance(other, Patient) is False:
            return False
        else:
            if (self.first_name == other.first_name
                    and self.last_name == other.last_name
                    and self.mrn == other.mrn
                    and self.age == other.age):
                return True
            else:
                return False

    def create_output(self):
        out_string = ""
        out_string += "Name: {} {}\n".format(self.first_name,
                                             self.last_name)
        out_string += "MRN: {}\n".format(self.mrn)
        if self.is_minor():
            status = "Minor"
        else:
            status = "Adult"
        out_string += "Status: {}\n".format(status)
        out_string += "Test Results: {}\n".format(self.tests)
        return out_string

    def is_minor(self):
        if self.age == 0:
            print("Didn't work")
            return None
        if self.age < 18:
            return True
        else:
            return False

    def add_test_result(self, test_name, test_value):
        new_result = (test_name, test_value)
        self.tests.append(new_result)

    def save(self):
        mongodb_patient = Patient.get_patient_from_db(self.mrn)
        mongodb_dict = {
            "_id": self.mrn,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "tests": self.tests,
            "blood_type": self.blood_type
        }
        if mongodb_patient is None:
            Patient.collection.insert_one(mongodb_dict)
        else:
            Patient.collection.replace_one(
                {"_id": self.mrn}, mongodb_dict
            )

    @classmethod
    def get_patient_from_db(cls, mrn):
        document = Patient.collection.find_one(
            {"_id": mrn}
        )
        if document is None:
            return None
        new_patient = Patient(
            document["first_name"],
            document["last_name"],
            document["_id"],
            document["age"],
            document["tests"],
            document["blood_type"]
        )
        return new_patient
