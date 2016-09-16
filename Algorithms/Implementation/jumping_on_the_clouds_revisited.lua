n,k = io.read("*number", "*number", "*l")
c = {}
for i=1,n do
    c[i] = io.read('*n') == 1
end

energy = 100 - (n/k)
for i=1,n,k do
    if c[i] then
        energy = energy - 2
    end
end

print(energy)


