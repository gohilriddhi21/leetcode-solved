def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

if __name__ == "__main__":
    print(fact(4)) # 4*3*2*1