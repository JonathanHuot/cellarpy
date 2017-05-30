import unittest
import cellar


class test_password(unittest.TestCase):
    def test_hash(self):
        x = cellar.password.hashpassword('foo', '1234')
        y = cellar.password.hashpassword('foo', '4321')
        z = cellar.password.hashpassword('bar', '4321')
        self.assertNotEqual(x, y)
        self.assertNotEqual(x, z)
        self.assertNotEqual(y, z)
