from flask import Flask, request, jsonify
from blood_analysis import analyze_generic_result

app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def server_status():
    return "Server is on until I turn it off"


@app.route("/info", methods=["GET"])
def get_info():
    msg = "This is the demonstration server for"
    msg += " BME 547."
    return msg


@app.route("/repeat_name", methods=["POST"])
def post_repeat_name():
    in_data = request.get_json()
    return in_data


@app.route("/check_HDL", methods=["POST"])
def post_check_HDL():
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    test_ranges = {"Normal": (60, 1000),
                   "Borderline Low": (40, 59),
                   "Low": (0, 39)}
    result = analyze_generic_result(hdl_value, test_ranges)
    return result


@app.route("/hdl/<hdl_value>/extra/<name>", methods=["GET"])
def get_check_HDL(hdl_value, name):
    hdl_value = int(hdl_value)
    test_ranges = {"Normal": (60, 1000),
                   "Borderline Low": (40, 59),
                   "Low": (0, 39)}
    result = analyze_generic_result(hdl_value, test_ranges)
    return "{} is {}".format(name, result)


@app.route("/add/<a>/<b>", methods=["GET"])
def get_add(a, b):
    answer = int(a) + int(b)
    return jsonify(answer)


if __name__ == "__main__":
    app.run()
