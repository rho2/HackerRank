n = io.read("*number", "*l")
A = {}
for i=1, n do
    A[i] = io.read('*n')
end

dis = {}
for i=1,n do
    for j=1,n do
        if(i ~= j and A[i] == A[j]) then
            dis[#dis+1] = math.abs(i - j)
        end
    end
end

table.sort(dis)
print(dis[1] or '-1')