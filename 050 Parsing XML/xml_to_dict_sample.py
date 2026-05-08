import xmltodict

with open("People_XML.xml", "r") as data:
    # Parse the data into an ElementTree object
    xml = xmltodict.parse(data.read())
# print(xml)
for e in xml['People']['Person']:
    print(e)