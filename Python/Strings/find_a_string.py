s, sub = input(), input()
print(sum(s[i:].startswith(sub) for i in range(len(s))))