n = io.read('*n')
k = io.read('*n')
q = io.read('*n')

arr = {}
for i=0,n-1 do
    arr[(i+k)%n] = io.read('*n')
end

for i=0,q-1 do
    print(arr[io.read('*n')])
end