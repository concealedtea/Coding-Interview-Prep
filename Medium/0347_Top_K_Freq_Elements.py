class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dictionary = {}
        for val in nums:
            if val in dictionary.keys():
                dictionary[val] += 1
            else:
                dictionary[val] = 1
        sortdict = sorted(dictionary.items(), key = lambda x: x[1], reverse = True)
        print(sortdict)
        ans, added = [0] * k, 0
        while added < k:
            ans[added] = sortdict[added][0]
            added += 1
        return ans
            
            
        