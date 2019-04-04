import json
import xml.etree.cElementTree as ET
import sys

def format_person(person):
    full_name = person['first_name'] + ' ' + person['last_name']
    avatar = person['avatar']
    base_info = {'Age' : person['age'], 'Birth date' : person['birth_date'], 'Birth place' : person['birth_place'], 'Gender' : person['gender']}
    interests = person['interests']
    skills = person['skills']
    formated_person = {'full-name' : full_name, 'avatar' : avatar, 'base-info' : base_info, 'interests' : interests, 'skills' : skills}
    return formated_person

def business_card(person):
    pass

def build_html(formated_person):

    html = ET.Element("html")
    head = ET.SubElement(html, "head")

    ET.SubElement(head, 'title').text = formated_person['full-name']
    ET.SubElement(head, 'link', {'rel' : "stylesheet", 'type' : "text/css", 'href' : "styles.css"})

    body = ET.SubElement(html, "body")

    for key, value in formated_person.items():
        tag = ''
        if key == 'full-name':
            tag = 'h1'
            sub = ET.SubElement(body, tag, {'class': str(key)})
            sub.text = str(value)
        elif key == 'avatar':
            tag = 'img'
            src = value
            sub = ET.SubElement(body, tag, {'class': str(key),'src' : src})
        else:
            tag = 'div'
            sub = ET.SubElement(body, tag, {'class': str(key)})

            if key == 'base-info':
                for k, v in value.items():
                    ET.SubElement(sub, 'p').text = str(k) + ': ' + str(v)

            if key == 'interests':
                ET.SubElement(sub, 'h2').text = str(key)
                ul = ET.SubElement(sub, 'ul')
                for interest in value:
                    ET.SubElement(ul, 'li').text = str(interest)

            if key == 'skills':
                ET.SubElement(sub, 'h2').text = str(key)
                ul = ET.SubElement(sub, 'ul')
                for skill in value:
                    text = ''
                    for k, v in skill.items():
                        text += str(v) + ' '
                    ET.SubElement(ul, 'li').text = text

    tree = ET.ElementTree(html)
    tree.write("business_card.html")


def main(filename):
    with open('data.json') as json_file:  
        data = json.load(json_file)

    people = data['people']
    for person in people:
        pass
    build_html(format_person(people[0]))

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)