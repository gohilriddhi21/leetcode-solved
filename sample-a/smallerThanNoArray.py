def main(nums: list[int]) -> list[int]:
    count = [0] * 102
    for i in nums:
        count[i] += 1
    
    for i in range(1, 102):
        count[i] += count[i - 1]
    
    return [count[i - 1] if i > 0 else 0 for i in nums]


if __name__ == '__main__':
    print(main([8, 1, 2, 2, 3])) # [4,0,1,1,3]