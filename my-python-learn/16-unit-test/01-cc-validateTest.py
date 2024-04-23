import unittest
from validate import *

class ValidateCcTest(unittest.TestCase):
    def test_validateCc_valid(self):
        result = validateCc(date(2025,2,2), 0)
        self.assertEqual('Valid', result)

    def test_validateCc_invalid(self):
        result = validateCc(date(2022,2,2), 0)
        self.assertEqual('Expired', result)

    def test_validateCc_Exp(self):
        with self.assertRaises(RuntimeError):
            result = validateCc(date(2022,2,2), 1)

if __name__ == '__main__':
    unittest.main()
