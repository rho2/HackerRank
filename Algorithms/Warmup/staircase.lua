n = io.read("*number", "*l")
hash = '#'
space = ' '
for i=1,n do
    s = string.rep(space, n-i)
    h = string.rep(hash, i)
    print(s .. h)
end