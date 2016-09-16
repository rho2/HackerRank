t = io.read('*number', '*l')

for i=1, t do
    n, m, s = io.read('*n', '*n', '*n', '*l')
    a = s + m - 1
    if(a > n) then
       a = a % n
        if(a == 0) then
            a = n
        end
    end
    print(a)
end