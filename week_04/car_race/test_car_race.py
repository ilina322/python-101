import unittest
from car_race import Car, Driver, Race, extract_data_from_file
class TestCarRace(unittest.TestCase):

    def test_when_car_is_converted_to_str_then_return_brand_and_model(self):
        car = Car('Opel', 'Astra', 100)
        expected_result = 'Opel Astra'
        self.assertEqual(str(car), expected_result)

    def test_when_driver_is_converted_to_str_then_return_name_and_brand_and_model(self):
        car = Car('Opel', 'Astra', 100)
        driver = Driver('Police', car)
        expected_result = 'Police drives Opel Astra'
        self.assertEqual(str(driver), expected_result)

    def test_when_driver_in_list_has_car_with_highest_speed_then_return_driver(self):
        car1 = Car('Opel', 'Corsa', 8)
        car2 = Car('BMW', 'GT', 12)
        car3 = Car('Citroen', 'C4', 9)
        driver1 = Driver('Police', car1)
        driver2 = Driver('Georgi', car2)
        driver3 = Driver('Ilina', car3)

        drivers = [driver1, driver2, driver3]
        race = Race(drivers, 1)
        expected_result = driver2

        self.assertEqual(str(expected_result), str(Race.find_fastest_driver(race)))

    def test_when_race_is_done_then_return_first_three_drivers_and_their_points(self):
        car1 = Car('Opel', 'Corsa', 8)
        car2 = Car('BMW', 'GT', 12)
        car3 = Car('Citroen', 'C4', 9)
        driver1 = Driver('Police', car1)
        driver2 = Driver('Georgi', car2)
        driver3 = Driver('Ilina', car3)

        drivers = [driver1, driver2, driver3]
        race = Race(drivers, 1)
        expected_result = {Driver.get_name(driver2): 8, Driver.get_name(driver3): 6, Driver.get_name(driver1): 4}
        self.assertEqual(expected_result, Race.results(race))

    def test_when_read_from_json_then_return_dict(self):
        data = extract_data_from_file('cars.json')
        self.assertTrue(isinstance(data, dict))


if __name__ == '__main__':
    unittest.main()