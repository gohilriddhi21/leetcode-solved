class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = list(zip(position, speed))
        pair.sort(reverse=True)
        
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

if __name__ == "__main__":
    target = 10
    position = [4,1,0,7]
    speed = [2,2,1,1]
    print(Solution().carFleet(target, position, speed))