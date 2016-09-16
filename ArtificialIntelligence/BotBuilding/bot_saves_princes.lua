n = io.read('*number','*l')

first = io.read('*l')
for _=1, n-2 do
    io.read('*l')
end
last = io.read('*l')

-- 0-1
-- ---
-- 2-3

corner = 0
if(first:sub(-1) == 'p') then
    corner = 1
elseif(last:sub(1,1) == 'p') then
    corner = 2
elseif(last:sub(-1) == 'p') then
    corner = 3
end

steps = (n-1)/2

if(corner < 2) then -- up
    for i=1,steps do
        print('UP')
    end
else -- go down
    for i=1,steps do
        print('DOWN')
    end
end

if(corner%2 == 0 ) then -- go left
    for i=1,steps do
        print('LEFT')
    end
else -- go RIGHT
    for i=1,steps do
        print('RIGHT')
    end
end