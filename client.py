import requests

server = "http://127.0.0.1:5000"

r = requests.get(server)
print(r.status_code)
print(r.text)

r = requests.post(server+"/repeat_name",
                  json="DAW74")
print(r.status_code)
print(r.text)

out_json = {"hdl_value": 30,
            "patient_name": "David"}
r = requests.post(server + "/check_HDL", json=out_json)
print(r.status_code)
print(r.text)

r = requests.get(server + "/add/2/3")
print(r.status_code)
print(r.text)
print(r.json())
