time = io.read()

h = tonumber(string.sub(time,0,2))
m = string.sub(time,4,5)
s = string.sub(time,7,8)

a = string.sub(time,-2)

if(a == 'PM' and h ~= 12) then
    h = h + 12
elseif(a == 'AM' and h == 12) then 
    h = 0  
end

print(string.format('%02d:%s:%s',h,m,s))