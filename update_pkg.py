import json

with open('backend/package.json', 'r') as f:
    data = json.load(f)

data['dependencies']['ejs'] = '^3.1.9'

with open('backend/package.json', 'w') as f:
    json.dump(data, f, indent=2)
print("Updated package.json")
