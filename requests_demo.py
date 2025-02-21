import requests

# server = "https://api.github.com"

# r = requests.get(server + "/repos/dward2/BME547/branches")
# print(r)
# print(type(r))
# print(r.status_code)
# print(r.text)
# if r.status_code != 200:
#     print("There was an error")
#     print(r.text)
# else:
#     data = r.json()
#     for branch in data:
#         print(branch["name"])

server = "http://vcm-43716.vm.duke.edu:5000"

student_data = {
   "name": "David Ward",
   "net_id": "daw74",
   "e-mail": "david.a.ward@duke.edu"
}

r = requests.post(server + "/student", 
                  json=student_data)
print(r.status_code)
print(r.text)

r =requests.get(server + "/list")
print(r.json())
