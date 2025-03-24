def round( n ):
    a = (n // 10) * 10
    b = a + 10
    return (b if n - a >= b - n else a)

if __name__ == "__main__":
    n = 33
    print(round(n))