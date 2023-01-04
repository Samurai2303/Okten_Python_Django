from unittest import TestCase

from ..services import calc


class CalcTestCase(TestCase):
    def test_plus(self):
        res = calc(1, 2, '+')
        self.assertEqual(res, 3)

    def test_minus(self):
        res = calc(1, 2, '-')
        self.assertEqual(res, -1)

    def test_multi(self):
        res = calc(1, 2, '*')
        self.assertEqual(res, 2)

    def test_division(self):
        res = calc(1, 2, '/')
        self.assertEqual(res, 0.5)
