import json

class Car:
    def __init__(self, brand, model, max_speed):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return str(self.brand) + ' ' + str(self.model)

class Driver:
    points = 0

    def __init__(self, name, car):
        self.name = name
        self.car = car

    def __str__(self):
        return str(self.name) + ' drives ' + str(self.car)

    def get_name(self):
        return str(self.name)

class Race:
    def __init__(self, drivers):
        self.drivers = drivers

    def find_fastest_driver(self):
        fastest_driver = Driver('', None)
        fastest_driver_speed = 0
        for driver in self.drivers:
            current_max_speed = driver.car.max_speed 
            if current_max_speed >= fastest_driver_speed:
                fastest_driver = driver
                fastest_driver_speed = current_max_speed
        return fastest_driver


    def results(self):
        first = self.find_fastest_driver()
        self.drivers.remove(first)
        second = self.find_fastest_driver()
        self.drivers.remove(second)
        third = self.find_fastest_driver()
        self.drivers.remove(third)

        first.points += 8
        second.points += 6
        third.points += 4

        return {Driver.get_name(first): first.points, Driver.get_name(second): second.points, Driver.get_name(third): third.points}

    def __str__(self):
        results = self.results()
        race_result = '###### START ######\n'
        for key, value in results.items():
            race_result += key + ': ' + str(value) + '\n'
        return race_result


class Championship:
    def __init__(self, name, race_number):
        self.name = name
        self.race_number = race_number

    def top3(self):
        pass


    def write_results(self, filename):
        result_file = open(filename , 'w')
        with result_file as outfile:
            json.dump(self.results(), outfile)
        print('success')



def extract_data_from_file(filename):
    file = open(filename , 'r')
    data = {}
    with file as outfile:
        data = json.load(outfile)
    return data



def main():
    data = extract_data_from_file('cars.json')
    drivers = [Driver(item['name'], Car(item['car'], item['model'], item['max_speed'])) for item in data['people']]
    race = Race(drivers)
    print(str(race))


if __name__ == '__main__':
    main()
