import unittest
def one_away(s1,s2):
    if len(s1) == len(s2):
        if s1 == s2: return True
        return isReplace(s1,s2)
    elif len(s1) + 1 == len(s2):
        return isRemove(s1,s2)
    elif len(s1) - 1 == len(s2):
        return isRemove(s2,s1)
    return False

def isReplace(s1, s2):
    totalDifs = False
    for ch1,ch2 in zip(s1,s2):
        if ch1 != ch2:
            if totalDifs: return False
            totalDifs += 1
    return True

def isRemove(s1, s2):
    totalDifs = False
    idx1, idx2 = 0,0
    while idx1 < len(s1) and idx2 < len(s2):
        if s1[idx1] != s2[idx2]:
            if totalDifs: return False
            totalDifs = True
            idx2 += 1
        else:
            idx1 += 1
            idx2 += 1
    return True

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