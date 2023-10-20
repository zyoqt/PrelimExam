import unittest

class name(unittest.TestCase):
    def test_name(self):
        a = 'MIGUEL'
        b = 'MIGUEL'
        self.assertEqual(a, b)

    def test_true(self):
        a = True
        b = True
        self.assertEqual(a, b)

if __name__ == '__main__':

    unittest.main()