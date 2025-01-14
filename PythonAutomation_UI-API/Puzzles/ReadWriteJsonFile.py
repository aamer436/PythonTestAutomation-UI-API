import json
from pathlib import Path

print(Path(__file__).resolve().parent.parent)
project_root=Path(__file__).resolve().parent.parent ### write parent as many times as you need to reach the project root

with open(str(project_root)+'/resources/ExampleJson1.json',mode='r') as f:
    data=json.load(f)
    print(data)

with open(str(project_root)+'/output/New_JsonFile.json',mode='w') as f:
    data={'person': {'name': 'John Doe', 'age': 30, 'address': {'street': '123 Main St', 'city': 'Anytown', 'zip': '12345'}, 'hobbies': [{'name': 'reading', 'type': 'indoor'}, {'name': 'traveling', 'type': 'outdoor'}]}}
    json.dump(data,f)
