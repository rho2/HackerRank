a = {}
b = {}
a[0],a[1],a[2] = io.read("*number", "*number", "*number", "*l")
b[0],b[1],b[2] = io.read("*number", "*number", "*number", "*l")

alice = 0
bob = 0

for i=0, 2, 1 do
    if(a[i] > b[i]) then
        alice = alice + 1
    elseif(b[i] > a[i]) then
        bob = bob + 1
    end
end

print(alice .. ' ' .. bob)