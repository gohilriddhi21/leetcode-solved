import heapq

def kth_largest_in_matrix(matrix, k):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0  # Handle empty matrix case

    if not (1 <= k <= rows * cols):
        print("k must be between 1 and rows * cols")
        return None
        

    heap = []  # Min-heap to store the k largest elements

    for i in range(rows):
        for j in range(cols):
            print("Pushed: ", matrix[i][j])
            heapq.heappush(heap, matrix[i][j])  # Add element to heap
            
            if len(heap) > k:
                print("Popped: ",heap[0])
                heapq.heappop(heap)  # Remove smallest element if heap size exceeds k
    return heap[0]  # The root of the min-heap is the kth largest element


if __name__ == "__main__":
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 3
    result = kth_largest_in_matrix(matrix, k)
    print(f"The {k}th largest element is: {result}")

    matrix2 = [[5]]
    k2 = 2
    result2 = kth_largest_in_matrix(matrix2, k2)
    print(f"The {k2}th largest element is: {result2}") 