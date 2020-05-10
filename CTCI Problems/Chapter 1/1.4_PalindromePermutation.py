import unittest, re
def pal_perm(s):
    s = " ".join(re.split("[^a-zA-Z]*", s)).lower().replace(" ","")
    dictionary = {}
    for char in s:
        if char in dictionary: dictionary[char] += 1
        else: dictionary[char] = 1
    numOdds = 0
    for key in dictionary:
        if dictionary[key] % 2 != 0: 
            if numOdds > 0: return False
            numOdds += 1
    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()