from flask import Flask, request, jsonify
from patient_class import Patient
import logging
from pymongo import MongoClient

app = Flask(__name__)


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    """Adds a new patient to the database

    The "/new_patient" route is called to add a new patient to
    the database.  This route expects a JSON-encoded dictionary
    with the following format:

    {"name": <str_patient_name>, "id": <int_patient_id>,
     "blood_type": <str_patient_blood_type>}

    where <str_patient_name> is a string containing the name of
     the patient, <int_patient_id> is an integer that is the
     patient's medical record number, and <str_patient_blood_type>
     is a string containing the patient's blood type.  The blood
     type must be an acceptable blood type.  This information is
     validated and then added to the database.  A response code of
     200 is returned if the patient is successfully added.  A
     response code of 400 is returned, along with an error message,
     if there was a problem with the request and the patient
     was not added

    Returns:
        str: Message about success or failure of request,
        int: Response code of 200 or 400
    """
    # Get the input data
    in_data = request.get_json()
    # Validate the input
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    check_results = validate_post_input(
        in_data, expected_keys, expected_types)
    if check_results is not True:
        return check_results, 400
    check_blood_type = validate_blood_type(in_data["blood_type"])
    if check_blood_type is not True:
        return check_blood_type, 400
    # Call helper functions to implement the route
    add_patient_to_db(in_data)
    # Return a response
    logging.info("Entry added: {}".format(in_data))
    answer = {"message": "Patient added",
              "data": in_data}
    return jsonify(answer), 200


def validate_post_input(in_data, expected_keys, expected_types):
    """Validates the dictionary that is received with POST requests

    The POST requests for this server receive JSON-encoded
    dictionaries with the needed input for the route.  This
    function checks that the needed keys can be found in the
    dictionary and that the values for each key are of the
    expected type.  The function will return True if all
    validation is successful.  It will return a string with an
    error message if something fails validation.

    Args:
        in_data (dict): The input dictionary received by the route
        expected_keys (list[str]): a list of strings with the
            key names that should be found in the input dictionary.
        expected_types (list[Type]): a list of data types, in the
            same order as the keys, that indicate the expected
            data type for value of the dictionary.

    Returns:
        bool: A value of True if all validation passes, or
        str: A string containins an error message if validation
            fails.
    """
    for ex_key, ex_type in zip(expected_keys, expected_types):
        if ex_key not in in_data:
            return "Key {} is not found in input.".format(ex_key)
        if type(in_data[ex_key]) is not ex_type:
            return ("The value for key {}".format(ex_key) +
                    " is not the expected type of {}.".format(ex_type))
    return True


def validate_blood_type(blood_type):
    valid_blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    if blood_type in valid_blood_types:
        return True
    else:
        return "Given blood type of {} is not valid.".format(blood_type)


def add_patient_to_db(in_data):
    """Adds patient to the database

    This function receives a dictionary containing patient information.
    That information is used to instantiate a Patient class instance.
    That instance is then appended to the global `db` variable.

    Args:
        in_data (dict): A dictionary containing patient information.
            See the documentation for the "/new_patient" route for
            its expected contents
    """
    first_name, last_name = in_data["name"].split(" ")
    new_patient = Patient(first_name, last_name,
                          in_data["id"],
                          blood_type=in_data["blood_type"])
    new_patient.save()


@app.route("/add_test", methods=["POST"])
def post_add_test():
    """Adds test result to a specific patient.

    This route is used to receive testing data for a specific
    patient and add that test result to the patient.
    The input to this route should be a dictionary as the following
    example:

    {"id": <int_patient_id>, "test_name": <str_test_name>",
    "test_result": <int_test_result>}

    where <int_patient_id> is an integer of the patient's medical
    record number, <str_test_name> is a string with the name of
    the test, and <int_test_result> is an integer with the value of
    the test result.

    The function validates that the correct information was received
    by the route and returns an error message if not.

    The function then finds the correct patient in the database
    using the mrn and then adds the test name and test result as
    a tuple to the test list of the patient.

    Returns:
        str, int: a string with a message about the success or
            failure of the request, and a response code of either
            200 or 400.
    """
    in_data = request.get_json()
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    check_input = validate_post_input(in_data,
                                      expected_keys,
                                      expected_types)
    if check_input is not True:
        return check_input, 400
    result = add_test_to_patient(in_data)
    if result is not True:
        return result, 400
    return "Test added", 200


def add_test_to_patient(in_data):
    patient = get_patient(in_data["id"])
    if patient is False:
        return "Patient not found"
    patient.add_test_result(in_data["test_name"],
                            in_data["test_result"])
    patient.save()
    return True


def get_patient(mrn):
    patient = Patient.get_patient_from_db(mrn)
    if patient is None:
        return False
    else:
        return patient


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_get_results(patient_id):
    """Obtains test results for the given patient id

    This variable URL route expects a patient medical record
    number to be added in place of <patient_id>.  This function
    first verifies that the provided <patient_id> is an integer.
    It then verifies that the patient exists in the database.
    If so, the list of test results is returned.  If not, an error
    message is return.

    Args:
        patient_id (str): A string that contains the patient_id
            extracted from the route URL.

    Returns:
        list, int:   A list of the test results for the specified
            patient and a response status code, or
        str, int:  A string containing an error message if there
            was a problem with the request and a response status code.
    """
    mrn = validate_patient_id(patient_id)
    if mrn is False:
        return "Given patient id is not an integer", 400
    patient = get_patient(mrn)
    if patient is False:
        return "Patient id of {} not found in database.".format(mrn), 400
    return jsonify(patient.tests), 200


def validate_patient_id(patient_id):
    try:
        mrn = int(patient_id)
    except ValueError:
        return False
    return mrn


def initialize_server():
    logging.basicConfig(filename="health_db_server.log",
                        filemode='w',
                        level=logging.INFO)
    connect_to_db()
    add_patient_to_db({"name": "Ann Ables",
                       "id": 1,
                       "blood_type": "A+"})
    
def connect_to_db():
    print("Connecting to database...")
    url = ("mongodb+srv://spring25:spring25@bme547.ba348.mongodb.net/"
           "?retryWrites=true&w=majority&appName=BME547")
    Patient.client = MongoClient(url)
    Patient.database = Patient.client["Class_Database"]
    Patient.collection = Patient.database["Patients"]
    print("Connection done")


if __name__ == "__main__":
    initialize_server()
    app.run()
