for i in range(int(input())):
    n = int(input())
    print( ~ ( ~ 1 << (n >> 1)) << n % 2)