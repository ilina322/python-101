import unittest
from oop_tasks import Bill

class TestOopTasks(unittest.TestCase):

    def test_when_str_returns_a_amount_bill(self):
        bill = Bill(10)
        expected_result = 'A 10$ bill!'
        self.assertEqual(str(bill), expected_result)

    def test_when_int_returns_amount(self):
        bill = Bill(10)
        expected_result = 10
        self.assertEqual(int(bill), expected_result)

    def test_when_repr_returns_amount_to_str(self):
        bill = Bill(10)
        expected_result = '10'
        self.assertEqual(repr(bill), expected_result)

    def test_when_two_bills_are_equal_then_return_true(self):
        bill1 = Bill(10)
        bill2 = Bill(10)
        self.assertTrue(bill1 == bill2)



if __name__ == '__main__':
    unittest.main()