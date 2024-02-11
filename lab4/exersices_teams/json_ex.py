import json

file_path = 'sample-data.json'

with open(file_path, 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:50} {:20} {:6} {:6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    mtu = item["l1PhysIf"]["attributes"]["mtu"]
    speed = item["l1PhysIf"]["attributes"]["speed"]
    print("{:50} {:20} {:6} {:6}".format(dn, "", speed, mtu))
