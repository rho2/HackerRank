n = io.read("*number", "*l")
c = {}
for i=0,n do
    c[i] = io.read('*n') == 0
end

count = 0
current = 0

while(current < n-1) do
    if(c[current + 2] and (n-current) > 2) then
        current = current + 2
    else 
        current = current + 1
    end
    count = count + 1
end

print(count)