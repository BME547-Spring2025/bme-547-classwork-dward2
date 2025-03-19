import requests

server = "http://127.0.0.1:5000"

patient_data = {"name": "David Ward",
                "id": 123,
                "blood_type": "O+"}

r = requests.post(server + "/new_patient",
                  json=patient_data)
print(r.status_code)
print(r.text)

test_data = {"id": 123, "test_name": "HDL", "test_result": 55}
r = requests.post(server + "/add_test",
                  json=test_data)
print(r.status_code)
print(r.text)

test_data = {"id": 123, "test_name": "LDL", "test_result": 42}
r = requests.post(server + "/add_test",
                  json=test_data)
print(r.status_code)
print(r.text)
