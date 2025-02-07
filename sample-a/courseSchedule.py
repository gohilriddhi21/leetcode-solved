class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preMap = {i:[] for i in range(numCourses)}
        for prerequisite in prerequisites:
            preMap[prerequisite[0]].append(prerequisite[1])

        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for neighbours in preMap[crs]:
                if not dfs(neighbours): return False

            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


if __name__ == "__main__":
    numCourses = 5
    prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4]]
    print(Solution().canFinish(numCourses, prerequisites)) # True