n = io.read("*number", "*l")
B = io.read()

count = 0 

for i in string.gmatch(B, "010") do
    count = count + 1
end

print(count)