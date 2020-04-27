import unittest
# This takes O(nlogn) + O(mlogm) where n and m are the lengths of each string 
# While this is not the most efficient method, this is certainly the fastest way to implement it
def checkPermutation1(s1, s2):
    return sorted(s1) == sorted(s2)

# Alternatively, we could use a dictionary to keep track of the occurances
# of each character and subtract the values while iterating through the 2nd string
# This will take O(n) + O(m) time and O(128) Space (assuming ASCII) where n and m are the
# lengths of each string 
def checkPermutation2(s1, s2):
    dictionary = {}
    for char in s1:
        if char in dictionary: dictionary[char] += 1
        else: dictionary[char] = 1
    for char in s2:
        if char in dictionary: dictionary[char] -= 1
        else: return False
    return True

class Test(unittest.TestCase):
    trueCases = [('hello', 'helol'), ('13hdm', 'dmh31'), ('wiek97', 'kiew79')]
    falseCases = [('hello', 'helo3l'), ('12345', '12346'), ('abdisj', 'klpoq')]
    def testPermutation(self):
        for case in self.trueCases:
            result1 = checkPermutation1(case[0], case[1])
            result2 = checkPermutation2(case[0], case[1])
            self.assertTrue(result1)
            self.assertTrue(result2)
        for case in self.falseCases:
            result1 = checkPermutation1(case[0], case[1])
            result2 = checkPermutation2(case[0], case[1])
            self.assertFalse(result1)
            self.assertFalse(result2)

if __name__ == "__main__":
    unittest.main()