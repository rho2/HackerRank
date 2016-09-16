n = io.read("*number", "*l")
a = {}
prim = 0
sec = 0
for i = 1,n do
    a[i] = {}
   for j = 1,n do
        a[i][j] = io.read("*number")
   end
   prim = prim + a[i][i]
   sec = sec + a[i][n-i+1]
end

print(math.abs(prim-sec))