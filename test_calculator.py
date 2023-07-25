from unittest import TestCase
from calculator import add


class Test(TestCase):
    def test_calculator_return_0_when_no_receive_numbers(self):
        self.assertEqual(add(), '0')

    def test_calculator_should_return_the_same_number_when_receive_only_one_number(self):
        self.assertEqual(add('1'), '1')

    def test_calculator_add_all_the_numbers_separated_by_commas(self):
        self.assertEqual(add('1,2,3'), '6')

    def test_calculator_add_all_the_numbers_separated_by_commas_and_newlines(self):
        self.assertEqual(add('1\n2,3'), '6')

    def test_calculator_send_a_error_when_there_are_two_delimiters_together(self):
        self.assertEqual(add('175.2,\n35'), 'Number expected but "\n" found at position 6.')

    def test_calculator_send_a_error_when_there_are_a_delimiter_at_the_end(self):
        self.assertEqual(add('1,3,'), 'Number expected but EOF found.')

    def test_calculator_add_the_numbers_with_custom_delimiters(self):
        self.assertEqual(add('//;\n1;2'), '3')
        self.assertEqual(add('//|\n1|2|3'), '6')
        self.assertEqual(add('//sep\n2sep3'), '5')

    def test_calculator_send_a_error_when_there_are_two_delimiter(self):
        self.assertEqual(add('//|\n1|2,3'), '\'|\' expected but \',\' found at position 3.')


"""
class Test(TestCase):
    def test_calculator(self):
        self.fail()
"""