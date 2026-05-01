from textwrap import indent

# import yaml
#
# #Method 1 - to read yaml file
# with open('sample.yaml', 'r+') as open_file:
#     data = yaml.safe_load(open_file)
#     print(type(data))
#     print(data['metadata']['labels']['app'])
#     data['metadata']['labels']['app'] = 'nkit'
#     open_file.seek(0)  # Move the cursor to the beginning of the file
#     yaml.safe_dump(data, open_file,)

import yaml

with open('sample.yaml', 'r+') as read_yaml:
    read_file = yaml.safe_load(read_yaml)
    print(read_file['spec']['replicas'])
    read_file['spec']['replicas'] = 4
    read_yaml.seek(0)
    yaml.safe_dump(read_file, read_yaml)
    # print(read_file)