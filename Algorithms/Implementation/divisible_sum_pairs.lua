n,k = io.read("*number", "*number", "*l")
a = {}
for i=1, n do
    a[i] = io.read('*n')
end
ans = 0
for i=1,n do
    for j=i+1,n do
        if(i<j and (a[i]+a[j])%k == 0) then
            ans = ans + 1
        end
    end
end
print(ans)