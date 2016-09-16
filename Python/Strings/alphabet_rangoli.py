import string

n = int(input())
w = 4*n - 3
abc = string.ascii_lowercase

save = {}
for i in range(n):
    c = abc[n-1-i]
    l = abc[n-1:n-1-i:-1]
    r = l[::-1]
    save[i] = '-'.join(list(l + c + r))
    print(save[i].center(w,'-'))
    
for i in range(n-2,-1,-1):
    print(save[i].center(w,'-'))