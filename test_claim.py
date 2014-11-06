from Claim import Claim, typedef
import unittest


class TestClaims(unittest.TestCase):

    def setUp(self):
        self.smallClaim = lambda x: x < 10
        self.largeClaim = lambda x: x > 10
        self.strClaim = lambda x: type(x) == str
        self.lenClaim = lambda x: len(x) == 15

    def test_single(self):
        simple = Claim(self.smallClaim)
        self.assertTrue(simple(5))
        self.assertFalse(simple(100))

    def test_iand(self):
        composite = Claim(self.strClaim)
        self.assertTrue(composite("help"))
        self.assertFalse(composite(3.6))
        other = Claim(self.lenClaim)
        composite &= other
        myStr = "Hello World!!!!"
        self.assertTrue(composite(myStr))

    def test_and(self):
        string = Claim(self.strClaim)
        length = Claim(self.lenClaim)
        composite = string & length
        self.assertTrue(composite("Hello World!!!!"))
        self.assertTrue(string("Help"))
        self.assertTrue(length([i for i in range(15)]))
        self.assertFalse(composite("help"))
        self.assertFalse(composite([i for i in range(15)]))

if __name__ == '__main__':
    unittest.main()
