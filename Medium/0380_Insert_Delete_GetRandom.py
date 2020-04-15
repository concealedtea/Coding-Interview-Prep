class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.pos = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.vals:
            self.vals.append(val)
            self.pos[val] = len(self.vals) - 1
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.vals: return False
        idx, last = self.pos[val], self.vals[-1]
        self.vals[idx], self.pos[last] = last, idx
        self.vals.pop(); self.pos.pop(val, 0)
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.vals[random.randint(0,len(self.vals) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()