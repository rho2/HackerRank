N, K = io.read('*number', '*number', '*l')
c = {}
luck = 0

for i=1, N do
    local l,t = io.read('*number', '*number', '*l')
    if(t == 1) then
        c[#c+1] = l
    else
        luck = luck + l
    end
end

table.sort(c)

for i=1, #c-K do
    luck = luck - c[i]
end


for i=#c-K + 1, #c do
    luck = luck + (c[i] or 0)
end

print(luck)