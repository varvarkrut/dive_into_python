import unittest
from week05_factorize import factorize
import sys


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        self.cases = ['string', 1.5]
        for b in self.cases:
            with self.subTest(case=b):
                self.assertRaises(TypeError, factorize, b)

    def negative(self):
        self.cases = [-1, -10, -100]
        for b in self.cases:
            with self.subTest(case=b):
                self.assertRaises(TypeError, factorize, b)

    def test_zero_and_one_cases(self):
        self.cases = [0, 1]
        for b in self.cases:
            with self.subTest(case=b):
                self.assertEqual(factorize(b), (b,))

    def test_simple_numbers(self):
        self.cases = [3, 13, 29]
        for b in self.cases:
            with self.subTest(case=b):
                self.assertEqual(factorize(b), (b,))

    def test_two_simple_multipliers(self):
        self.cases = {6: (2, 3), 26: (2, 13), 121: (11, 11)}
        for b in self.cases:
            with self.subTest(case=b):
                self.assertEqual(factorize(b), self.cases.get(b))

    def test_many_multipliers(self):
        self.cases = {1001: (7, 11, 13), 9699690: (2, 3, 5, 7, 11, 13, 17, 19)}


"""def sort_test_suite():
    suite = unittest.TestSuite()
    '''suite.addTest(TestFactorize('negative'))'''
    suite.addTest(TestFactorize('test_wrong_types_raise_exception'))
    suite.addTest(TestFactorize('test_zero_and_one_cases'))
    suite.addTest(TestFactorize('test_simple_numbers'))
    suite.addTest(TestFactorize('test_two_simple_multipliers'))
    suite.addTest(TestFactorize('test_many_multipliers'))
    return suite
"""


'''if True:  # __name__ == "__main__":
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=1)
    test_suite = sort_test_suite()
    runner.run(test_suite)'''
