s = io.read()
::start::
for i=2, s:len() do
    if(s:sub(i,i)== s:sub(i-1,i-1)) then
        s = s:gsub(s:sub(i,i)..s:sub(i,i),'')
        goto start
    end
end
if(s:len() == 0) then s = nil end
    
print(s or 'Empty String')