# Using a table to hold all seen values and updating if seen we can reduce the runtime
# to at most the number of values in the table * the number of characters in n
# Runtime: O(n)
# Space Complexity: Size of Character alphabet
def isUnique(s):
    asciiTable = [False] * 128
    for char in s:
        if asciiTable[ord(char)] == True: 
            return False
        asciiTable[ord(char)] = True
    return True

# Test Cases for isUnique
result = isUnique("hello")
print("hello: " + str(result))
result2 = isUnique("helo")
print("helo: " + str(result2))