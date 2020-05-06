import unittest
def one_away(s1,s2):
    if len(s1) == len(s2):
        if s1 == s2: return True
        if isReplace(s1,s2): return True
    if len(s1) > len(s2):
        if isRemove(s1,s2): return True
    if len(s1) > len (s2): 
        if isRemove(s2, s1): return True
    return False

def isReplace(s1, s2):
    totalDifs = 0
    for idx, char in enumerate(s1):
        if char != s2[idx]: totalDifs += 1
    return totalDifs <= 1

def isRemove(s1, s2):
    totalDifs = 0
    # Make sure s1 is longer, if not, swap their positions
    if len(s1) < len(s2): s1,s2 = s2,s1


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()