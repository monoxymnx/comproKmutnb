import json

data = {"name": "Alice", "age":25}
json_string = json.dumps(data)
print(json_string)

parsed_data = json.loads(json_string)
print(parsed_data)
print(parsed_data["name"])
print(parsed_data["age"])