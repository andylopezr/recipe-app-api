"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Tests the calc module"""

    def test_add_numbers(self):
        """Tests adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        """Tests subtracting numbers together"""
        res = calc.sub(15, 10)

        self.assertEqual(res, 5)
