t = io.read("*number", "*l")

a = t/3.0 + 1.0
a = math.log(a)/math.log(2)
a = math.ceil(a)

b = 3 * (math.exp(math.log(2)*(a))-1)

c = b - t + 1

print(math.ceil(c))