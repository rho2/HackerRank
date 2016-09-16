import string

s = input().strip().lower()

for a in string.ascii_lowercase:
    if(not(a in s)):
        print('not pangram')
        break
else:
    print('pangram')
