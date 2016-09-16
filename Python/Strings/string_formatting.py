a = int(input())
f = '{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}'

print('\n'.join([f.format(i+1, w=a.bit_length()) for i in range(a)]))