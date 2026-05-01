import json

with open('role.json', 'r+') as open_file:
    data = json.load(open_file)
    print(data['Statement'][0]['Effect'])
    data['Statement'][0]['Effect'] = 'DENY'
    open_file.seek(0)
    json.dump(data,open_file, indent=4)
    open_file.truncate()

