#Simply read the file

try:
    open_file = open('DmmyData.txt', 'r')
    print(open_file.read())
except Exception as e:
    print("Encountered error", e)

finally:
    print("Closing file")
    open_file.close()
