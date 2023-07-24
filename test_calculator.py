from unittest import TestCase
from calculator import calculator


class Test(TestCase):
    def test_calculator_return_0_when_no_receive_numbers(self):
        self.assertEqual(calculator(), '0')

    def test_calculator_should_return_the_same_number_when_receive_only_one_number(self):
        self.assertEqual(calculator('1'), '1')

    def test_calculator_add_all_the_numbers_separated_by_commas(self):
        self.assertEqual(calculator('1,2,3'), '6')


"""
class Test(TestCase):
    def test_calculator(self):
        self.fail()
"""