t = io.read("*number", "*l")
for tt=1, t do
    s, k = io.read("*number", "*number", "*l")
    a = 0
    for ss = 1, s do
        if(io.read('*n') <= 0) then
            a = a + 1
        end
    end
    
    if(a >= k) then
        print('NO')
    else
        print('YES')
    end
end
