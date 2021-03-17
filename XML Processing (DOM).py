#DOM module work with dom trees. They view xml file as trees and every element is a branch in it 

import xml.dom.minidom

domtree = xml.dom.minidom.parse('data.xml')
group = domtree.documentElement

persons = group.getElementsByTagName('person')

for person in persons:
    print('----PERSON----')
    if person.hasAttribute('id'):
        print('ID: {}'.format(person.getAttribute('id')))

    print('Name: {}'.format(person.getElementsByTagName('name')[0].childNodes[0].data))
    print('Age: {}'.format(person.getElementsByTagName('age')[0].childNodes[0].data))
    print('Weight: {}'.format(person.getElementsByTagName('weight')[0].childNodes[0].data))
    print('Height: {}'.format(person.getElementsByTagName('height')[0].childNodes[0].data))

#Manipulating the xml file
persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = 'Rhee'
persons[0].setAttribute('id', '100')
persons[3].getElementsByTagName('age')[0].childNodes[0].nodeValue = '24'
domtree.writexml(open('data.xml', 'w'))

#Creating new elements 
newperson = domtree.createElement('person')
newperson.setAttribute('id', '6')

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Katie Macharia'))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('25'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('49'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('155'))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)
domtree.writexml(open('data.xml', 'w'))
