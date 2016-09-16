n = io.read("*number", "*l")
pos = 0
neg = 0
zeros = 0
for i = 1,n do
   a = io.read("*number")
   if(a > 0) then
        pos = pos + 1
   elseif(a<0) then
        neg = neg + 1
   else 
        zeros = zeros + 1
   end
end
print(pos/n)
print(neg/n)
print(zeros/n)