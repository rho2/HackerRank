A = set(input().split())

for _ in range(int(input())):
    B = set(input().split())
    if(not A.issuperset(B)):
        print(False)
        break
else: 
    print(True)