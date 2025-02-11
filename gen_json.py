import json

data = {
    "name": "Jenkins",
    "task": "Pipeline Demo",
    "status": "Success"
}

with open("output.json", "w") as f:
    json.dump(data, f)

print("JSON file 'output.json' has been created successfully.")
