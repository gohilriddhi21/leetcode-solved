def main(nums):
    # # 1
    # nums.sort()
    # for i, v in enumerate(nums):
    #     print(i, v)
    #     if i != v:
    #         print("returning v-1")
    #         return v-1
    #     if v == len(nums)-1:
    #         print("returning v+1")
    #         return v+1
    
    # 2
    return sum(range(len(nums)+1)) - sum(nums)

if __name__ == "__main__":
    nums = [0, 1]
    print(main(nums))