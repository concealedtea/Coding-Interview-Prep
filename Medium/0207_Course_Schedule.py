class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def hasCycle(node):
            if node in exploring:
                return True
            if node in explored:
                return False
            exploring.add(node)
            for neighbor in allClasses[node]:
                if hasCycle(neighbor): return True
            exploring.remove(node)
            explored.add(node)
            return False
                
        allClasses = collections.defaultdict(list)
        for s, e in prerequisites:
            allClasses[s].append(e)
        exploring, explored = set(), set()
        for clss in list(allClasses):
            if clss not in explored:
                if hasCycle(clss): 
                    return False
        return True
            
        