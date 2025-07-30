with open('./DummyData.txt', 'r') as read_file, open('Output.txt', 'w') as out_file:
    for line in read_file:
        print(line)
        if 'error' in line or 'warning' in line:
            out_file.write(line)
