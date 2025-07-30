import yaml

from FileHandling.ReadFile import open_file

#Method 1 - to read yaml file
with open('sample.yaml', 'r') as open_file:
    data = yaml.safe_load(open_file)
    print(type(data))
    print(data['metadata']['labels']['app'])


