n, k = io.read("*number", "*number", "*l")

r = {}
for i = 0, k do
  r[i] = 0
end

for i=1, n do
    m = io.read('*n') % k
    r[m] = r[m] + 1
end

count = 0

if r[0] > 0 then
    count = count + 1
end

if k % 2 == 0 and r[k/2] > 0 then
   count = count + 1
   r[k/2] = 0
end

for i = 1, math.floor( k / 2 ) do
  count = count + math.max(r[i], r[k - i])  
end

print (count)