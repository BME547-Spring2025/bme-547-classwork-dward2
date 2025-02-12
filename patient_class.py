class Patient:

    def __init__(self, first_name, last_name,
                 mrn, age=0, tests=None):
        self.first_name = first_name
        self.last_name = last_name
        self.mrn = mrn
        self.age = age
        if tests is None:
            self.tests = []
        else:
            self.tests = tests

    def __str__(self):
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
