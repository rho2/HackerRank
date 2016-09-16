n, d = io.read('*number', '*number', '*l')
nums = {}       -- list of all number
is = {}         -- boolean if index is in nums

for i=1, n do
    local n = io.read('*n')
    nums[i] = n
    is[n] = true
end

count = 0

for a,b in pairs(nums) do
    if(is[b+d] and is[b+d+d]) then
        count = count + 1
    end
end

print(count)