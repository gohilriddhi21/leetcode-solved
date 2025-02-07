import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        N = len(matrix)

        minHeap = []
        for r in range(min(k, N)):
            print("r: ", r)
            minHeap.append((matrix[r][0], r, 0))
            print("added: ", matrix[r][0])

        print(minHeap)
        heapq.heapify(minHeap) 
        print(minHeap)

        while k:
            element, r, c = heapq.heappop(minHeap)
            print("element popped: ", element, r, c)
            if c < N - 1:
                print("pushed: ", matrix[r][c+1])
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
            k -= 1 
        return element

if __name__ == "__main__":
    print(Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 5))