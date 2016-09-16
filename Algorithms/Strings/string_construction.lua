n = io.read("*number", "*l")

for a=1, n do
    s = io.read()
    count = 0
    while(s:len() > 0) do
        c = s:sub(1,1)
        s = s:gsub(c, '')
        count = count + 1
    end
    print(count)
end
