from django.test import SimpleTestCase

from app import calc


class  CalcTests(SimpleTestCase):
    def test_add_number(self):
        res = calc.add(6, 4)
        self.assertEqual(res, 10)

    def test_sub_number(self):
        res = calc.sub(5, 2)
        self.assertEqual(res, 3)
