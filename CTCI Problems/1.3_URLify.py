import unittest
def URLify(string, length):
    new_idx = len(string)
    for i in reversed(range(length)):
        if string[i] == ' ':
            string[new_idx - 3:new_idx] = '%20'
            new_idx -= 3
        else:
            string[new_idx - 1] = string[i]
            new_idx -= 1
    return string

class Test(unittest.TestCase):
    # Test Cases
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = URLify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()