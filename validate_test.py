import unittest
from validate import IdValidate

class ValidTest (unittest.TestCase):
 
    def test_value(self):
        self.assertRaises(ValueError, IdValidate,-3)

