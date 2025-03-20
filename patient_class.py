class Patient:
    """Patient data record connected to MongoDB

    This class serves the dual role of handling and using the
    connection with MongoDB as well as acting as the data
    structure to hold a single patient record.  The MongoClient
    instance and links to the appropriate database and collection
    in MongoDB are stored in class attributes.  The specific
    information about a single patient is stored in instance
    attributes.

    Class Attributes
        client (pymongo.MongoClient): the client connection to the
                                      MongoDB server
        database (pymongo.Database): connection to the appropriate
                                     database in MongoDB
        collection (pymongo.Collection): connection to the appropriate
                                         document collection in the
                                         database

    Instance Attributes
        first_name (str): patient's first name
        last_name (str): patient's last name
        mrn (int): patient's medical record number.  Also acts as the
                   primary key ("_id") in MongoDB.
        age (int): patient's age
        tests (list): a list of tuples containing a test name and result
        blood_type (str): patient's blood type
    """

    client = None
    database = None
    collection = None

    def __init__(self, first_name, last_name,
                 mrn, age=0, tests=None, blood_type=None):
        """Instantiates an instance of Patient Class

        The __init__ function takes as input the information about
        the patient to be created.  These inputs are then assigned
        to the appropriate instance attributes.

        Args:
            first_name (str): patient's first name
            last_name (str): patient's last name
            mrn (int): patient's medical record number
            age (int, optional): patient's age.  Defaults to 0 if not given.
            tests (list, optional):  List of tuples with patient test results.
                                     Defaults to empty list if not given.
            blood_type (str, optional):  patient's blood type.  Defaults to
                                         None if not given.

        """
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
        """Provides string representation of the class

        When a class instance is printed or displayed in a debugger,
        this function defines that will be displayed.  It will
        display the name of the class, the instance mrn number, and
        the instance first and last name.
        """
        return "Patient, mrn={}, {} {}".format(self.mrn,
                                               self.first_name,
                                               self.last_name)

    def __eq__(self, other):
        """Defines equality for two instances of the class.
        """
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
        """Generates output string with info on the patient"""
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
        """Returns True or False in answer to whether patient
           is a minor"""
        if self.age == 0:
            print("Didn't work")
            return None
        if self.age < 18:
            return True
        else:
            return False

    def add_test_result(self, test_name, test_value):
        """Add test results to the patient information

        This method receives a test name and its value for a
        test conducted on a patient.  That information is then
        added as a tuple to the patient test list.

        Args:
            test_name (str): the name of the test performed
            test_value (int or float): the result of the test performed
        """
        new_result = (test_name, test_value)
        self.tests.append(new_result)

    def save(self):
        """Saves the patient information in the MongoDB Database

        This method takes all of the information for the specific
        patient in the class instance and saves it into the MongoDB
        database.  First, the method calls the class method
        "get_patient_from_db" and checks to see if a patient with the
        mrn number already exists in the database.  It then creates
        a dictionary with the key:value pairs needed for storing
        information in MongoDB.  Since the mrn is the primary key in
        the MongoDB database, it is assigned the '_id' key.
        Then, if a patient with the mrn does not exist, a new patient
        document is inserted into the MongoDB collection stored in the
        class attribute "collection". If a patient already exists in
        the database with the mrn number, that document is replaced
        in MongoDB with the new patient information.
        """
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
        """Gets patient information from MongoDB

        This class attribute is used to obtain patient information
        from the MongoDB database.  First, it uses the mrn received
        as a parameter as a search parameter in the MongoDB collection.
        Since the mrn is the primary key, the '_id' key is used for the
        search.

        If no document is found, this method returns None.  If a document
        is found, the information in that document is used to instantiate
        a new Patient class and this class instance is then returned.

        Args:
            mrn (int): the medical record number of the patient to find

        Returns:
            Patient: a Patient instance containing information on the
                     desired patient, or
            NoneType: None if no patient is found.
        """
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

    @classmethod
    def clear_database(cls):
        """Deletes all documents in the collection"""
        Patient.collection.delete_many({})
