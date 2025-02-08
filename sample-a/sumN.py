def recursiveSum(i, sum):
    if i < 0:
        print(sum)
        return

    recursiveSum(i-1, sum+i)

def main():
    n = 5
    recursiveSum(5, 0)


if __name__ == '__main__':
    main()