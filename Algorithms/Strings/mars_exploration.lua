s = io.read()
count = 0
p = 'SOS'
for i in string.gmatch(s, "%u%u%u") do
    for j=1,3 do
        if(i:sub(j,j) ~= p:sub(j,j)) then
            count = count + 1
        end
    end
end
print(count)