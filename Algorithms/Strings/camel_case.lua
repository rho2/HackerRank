s = io.read()
count = 0
for i in string.gmatch(s, "%l+") do
  count = count + 1
end
print(count)
