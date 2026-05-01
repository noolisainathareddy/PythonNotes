import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')

root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

for child in root:
    print(child.tag, child.attrib)

