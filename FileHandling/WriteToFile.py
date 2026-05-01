import pathlib

path = pathlib.Path('.env')

print(path.read_text())

print(path.read_bytes())
# with open('.env', 'w') as update_file:
#     update_file.write('env=STAGE')
