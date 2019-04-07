import unittest
from queries import parse_csv

class TestQueries(unittest.TestCase):
    def test_when_csv_is_parsed_then_return_list_of_people(self):
        people = parse_csv('example_data.csv')
        self.assertTrue(isinstance(people, list))

    def test_when_csv_is_parsed_then_returned_list_contains_dicts(self):
        people = parse_csv('example_data.csv')
        self.assertTrue(isinstance(people[1], dict))


if __name__ == '__main__':
    unittest.main()