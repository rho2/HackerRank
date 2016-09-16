n = io.read("*number", "*l")
arr_temp = io.read()
sum = 0
for token in string.gmatch(arr_temp, "[^%s]+") do
   sum = sum + tonumber(token)
end

print(sum)