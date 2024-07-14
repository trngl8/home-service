import unittest
from validator import Validator

class ValidatorTest(unittest.TestCase):

    def test_is_empty(self):
        validator = Validator({"name" : "Ivan", "empty_field" : ""})
        self.assertTrue(validator.is_not_empty("name"))
        self.assertFalse(validator.is_not_empty("empty_field"))

    
    def test_is_integer(self):
        validator = Validator({"bedrooms" : "5", "name" : "John"})
        self.assertTrue(validator.is_integer("bedrooms"))
        self.assertFalse(validator.is_integer("name"))


    def test_is_in_range(self):
        validator = Validator({"electricity" : "200"})
        self.assertTrue(validator.is_in_range("electricity", 10, 500))
        self.assertFalse(validator.is_in_range("electricity", 10, 100))
        self.assertFalse(validator.is_in_range("electricity", 300, 600))
