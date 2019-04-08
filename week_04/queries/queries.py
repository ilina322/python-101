import csv

#names of columns in csv
#full_name, favourite_color, company_name, email, phone_number, salary

def parse_csv(filename):
    people = []
    with open(filename) as data:
        reader = csv.reader(data)
        keys = next(reader)
        for row in reader:
            person = {keys[i]:row[i] for i in range(len(keys))}
            people.append(person)
    return people

def check_requirements(person, requirements):
    passes = True
    for key, value in requirements.items():
        if '__' in key:
            args = key.split('__')
            if args[1] == 'startswith':
                if not person[args[0]].startswith(value):
                    passes = False
            elif args[1] == 'contains':
                if not value in person[args[0]]:
                    passes = False
        else:
            if person[key] != value:
                passes = False
    return passes

def filter(filename, **kwargs):
    people = parse_csv(filename)
    filtered_people = []

    for person in people:
        passes = check_requirements(person, kwargs)
        if passes:
            filtered_people.append(person)

    return filtered_people

def count(filename, **kwargs):
    people = parse_csv(filename)
    people_count = 0

    for person in people:
        passes = check_requirements(person, kwargs)
        if passes:
            people_count += 1

    return people_count

def first(filename, **kwargs):
    people = parse_csv(filename)

    for person in people:
        passes = check_requirements(person, kwargs)
        if passes:
            return person

    return None


def main():
    print(filter('example_data.csv', favourite_color='olive'))

if __name__ == '__main__':
    main()
