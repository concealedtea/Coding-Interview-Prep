import unittest
def string_compression(s):
    compressed, counter = [], 0
    for idx, char in enumerate(s):
        if idx != 0 and s[idx] != s[idx - 1]:
            compressed.append(s[idx-1] + str(counter))
            counter = 0
        counter += 1
    compressed.append(s[-1] + str(counter))
    return min(s, ''.join(compressed), key = len)

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()