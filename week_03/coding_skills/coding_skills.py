import sys
import json

def coding_skills(people):
    languages = ['C++', 'PHP', 'Python', 'C#', 'Haskell', 'Java', 'JavaScript', 'Ruby', 'CSS', 'C']
    max_levels = {}
    for language in languages:
        max_level = 0
        best_person = ''
        for person in people:
            name = person['first_name'] + ' ' + person['last_name']
            skills = person['skills']
            for skill in skills:
                if skill['name'] == language and skill['level'] > max_level:
                    max_level = skill['level']
                    best_person = name
        max_levels[language] = best_person
    return max_levels


def main():
    filename = sys.argv[1]
    with open(filename) as data:
        people = json.load(data)['people']
    print(coding_skills(people))

if __name__ == '__main__':
    main()