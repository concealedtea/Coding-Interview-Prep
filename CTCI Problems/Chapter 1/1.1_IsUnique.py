# Using a table to hold all seen values and updating if seen we can reduce the runtime
# to at most the number of values in the table * the number of characters in n
# Runtime: O(n)
# Space Complexity: Size of Character alphabet
import unittest
def isUnique(s):
    # Assuming total of 128 characters possible, ask if more?
    asciiTable = [False] * 128
    for char in s:
        if asciiTable[ord(char)] == True: 
            return False
        asciiTable[ord(char)] = True
    return True

# Test Cases for isUnique
class Test(unittest.TestCase):
    trueCases = ['abcd', 'ab3idj', '']
    falseCases = ['abccd', '3ijzdo3h', '(()']
    
    def test_unique(self):
        for case in self.trueCases:
            result = isUnique(case)
            self.assertTrue(result)
        for case in self.falseCases:
            result = isUnique(case)
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()