n,m = io.read("*number", "*number", "*l")
c = {}
for i=1, m do
   c[i] = io.read('*n')
end


if n == m then
    d = 0
    goto ende
end

table.sort(c)
d = 0
for i=2, m do
    d = math.max(c[i]-c[i-1], d) 
end
d = d/2
if(c[m] ~= n-1) then
    d = math.max(d, n-1 - c[m])
end

if(c[1] ~= 0) then
    d = math.max(d, c[1])
end

::ende::
print(math.floor(d))