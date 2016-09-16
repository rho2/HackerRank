x1,v1,x2,v2 = io.read("*number", "*number", "*number","*number", "*l")

if((x2 - x1) % (v2 - v1) == 0 and v2 < v1) then
    print('YES')
else
    print('NO')
end
