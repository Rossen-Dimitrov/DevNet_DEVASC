# import xml.etree.ElementTree as ET
from lxml import etree as ET

# Get the XML file data
with open("People_XML.xml", "r") as data:
    #Parse the data into an ElementTree object
    xml = ET.parse(data)

#Get the 'root' Element object from the ElementTree
root = xml.getroot()
print(f"Root element is: {root}")

#Iterate trough each child of the root Element
for element in root:
    #print the stringified version of the element
    print(f"Stringified element: {ET.tostring(element)}")
    # print the 'Id' attribute of each Element
    print(element.get("Id"))
    for person in root:
        # Намира тага FirstName вътре в Person и взима неговия текст
        first_name = person.findtext('FirstName')
    # for sub_element in element:
    #     # print(ET.tostring(sub_element))
    #     print(f"Sub Element {sub_element}")

for person in root:
    # Finds the FirstName tag in Person and gets its text
    first_name = person.findtext('FirstName')
    print(f"First Name: {first_name}")