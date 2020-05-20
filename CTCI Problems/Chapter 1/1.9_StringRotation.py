import unittest
# If s1 can be divided into 2 parts, x and y
# s2 must be able to be constructed yx
# thus, yx must be a substring of xyxy
# So if we take xy + xy and s2 is a substring, then s2 must be a rotation of s1
def string_rotation(s1, s2):
    combined = s1 + s1
    return isSubstring(combined, s2)

# Helper method O(longer one)
def isSubstring(s1, s2):
    # Swap so s1 is shorter
    if len(s1) > len(s2): 
        s2,s1 = s1,s2
    # For each index at s2, see if the following chars match s1
    for i in range(len(s2)):
        if s2[i:i + len(s1)] == s1: return True
    return False

class Test(unittest.TestCase):
    data = [(["waterbottle", "erbottlewat"], True),
    (["waterbottle", "erobttlewat"], False),
    (["foo", "bar"], False)]
    def test_string_rotation(self):
        for [test_cases, expected] in self.data:
            actual = string_rotation(test_cases[0], test_cases[1])
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()