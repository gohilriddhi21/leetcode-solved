import math 

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        # brute force
        speed = 1
        while True:
            total_time = 0
            print(f"\nK: {speed}")
            for pile in piles:
                total_time += math.ceil(pile / speed)
                print(f"\tPile: {pile} | Time: {pile / speed}")
            if total_time <= h:
                return speed
            speed += 1
            print(f"Total Time: {total_time}")
        return speed


if __name__ == "__main__":
    piles = [3, 6, 7, 11] 
    h = 8
    print(Solution().minEatingSpeed(piles, h)) # 2
