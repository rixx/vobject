import unittest

from vobject.base import readComponents


def get_test_file(path):
    """
    Helper function to open and read test files.
    """
    filepath = "test_files/{}".format(path)
    f = open(filepath, 'r')
    text = f.read()
    f.close()
    return text


class TestVobject(unittest.TestCase):

    def setUp(self):

        self.simple_test_cal = get_test_file("simple_test.ics")

    def test_readComponents(self):
        cal = next(readComponents(self.simple_test_cal))

        self.assertEqual(str(cal), "<VCALENDAR| [<VEVENT| [<SUMMARY{'BLAH': ['hi!']}Bastille Day Party>]>]>")
        self.assertEqual(str(cal.vevent.summary), "<SUMMARY{'BLAH': ['hi!']}Bastille Day Party>")

    """def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)
    """

if __name__ == '__main__':
    unittest.main()
