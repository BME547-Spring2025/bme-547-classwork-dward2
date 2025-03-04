from flask import Flask, request, jsonify
from patient_class import Patient
import logging

app = Flask(__name__)

db = []


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
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
    answer = {"message": "Patiend added", 
              "data": in_data}
    return jsonify(answer), 200


def validate_post_input(in_data, expected_keys, expected_types):
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
    first_name, last_name = in_data["name"].split(" ")
    new_patient = Patient(first_name, last_name, 
                          in_data["id"],
                          blood_type=in_data["blood_type"])
    db.append(new_patient)


@app.route("/add_test", methods=["POST"])
def post_add_test():
    """Adds test to a specific patient.

    This route is used to receive testing data for a specific
    patient and add that test result to the patient.
    The input to this route should be a dictionary as the following
    example:

    {"id": <int>, "name": <str>", "blood_type": <str>}

    Further explanation
    
    
    
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
    return "Patient added", 200


def add_test_to_patient(in_data):
    patient = get_patient(in_data["id"])
    if patient is False:
        return "Patient not found"
    patient.tests.append((in_data["test_name"],
                          in_data["test_result"]))
    return True


def get_patient(mrn):
    for patient in db:
        if patient.mrn == mrn:
            return patient
    return False


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_get_results(patient_id):
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
    add_patient_to_db({"name": "Ann Ables",
                       "id":1,
                       "blood_type": "A+"})
    

if __name__ == "__main__":
    initialize_server()
    app.run()
    