from datetime import datetime

for _ in range(int(input())):
    t1 = datetime.strptime(input(), '%a %d %b %Y %X %z')
    t2 = datetime.strptime(input(), '%a %d %b %Y %X %z')
    print(abs(int((t1-t2).total_seconds())))