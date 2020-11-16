#
# JSON
#

import json

# convert JSON data to Python objects
json_obj = '{"Name": "David", "Class": "I", "Age": 6}'
python_obj = json.loads(json_obj)
print("\nJSON data: ")
print(python_obj)
print("\nName: ", python_obj["Name"])
print("Class:", python_obj["Class"])
print("Age", python_obj["Age"])

# convert Python objects to JSON data
# Python object
python_obj = {
    "name": "David",
    "class": "I",
    "age": 6
}
print(type(python_obj))
# convert into JSON
j_data = json.dumps(python_obj)
# result is a JSON string
print(j_data)

#  Python objects into JSON strings
python_dict = {"name": "David", "age": 6, "class": "I"}
python_list =["Red", "Green", "Black"]
python_str = "Python Json"
python_int = 1234
python_float = 21.34
python_t = True
python_f = False
python_n = None
json_dict = json.dumps(python_dict)
json_list = json.dumps(python_list)
json_str = json.dumps(python_str)
json_num1 = json.dumps(python_int)
json_num2 = json.dumps(python_float)
json_t = json.dumps(python_t)
json_f = json.dumps(python_f)
json_n = json.dumps(python_n)
print("json_dict: ", json_dict, "\njson_list: ", json_list, "\njson_str: ", json_str)
print("json_num1: ", json_num1, "\njson_num2: ", json_num2)
print("json_t: ", json_t)
print("json_f: ", json_f)
print("json_n: ", json_n)

# convert Python dictionary objects to JSON data
j_str = {"4": 5, "6": 7, "1": 3, "2": 4}
print("Original String: ", j_str)
print("\nJSON data: ", json.dumps(j_str, sort_keys=True, indent=4))


# create a new JSON file from an existing JSON file
with open("resources/states.json") as f:
    state_data = json.load(f)  # reads JSON data and store them in state_data
new_states_data = json.dumps(state_data)
print(new_states_data)

