n = io.read("*number", "*l")
arr = {}
for i=1, n do
    arr[i] = io.read('*n')
end

while(#arr > 0) do
    print(#arr)
    table.sort(arr)
    len = arr[1]
    temp = {}
    for a in pairs(arr) do
        arr[a] = arr[a] - len
        if(arr[a] > 0) then
            temp[#temp+1] = arr[a]
        end
    end
    arr = temp
end