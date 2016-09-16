n = io.read('*number', '*l')

for a=1,n do
    local word = io.read()
    local chars = {}
    local ans

    word:gsub(".",function(a) table.insert(chars,a) end)

    for i=#chars-1,1,-1 do
        local jj,M
        for j=i+1,#chars do
            if chars[j] > chars[i] and (not M or chars[j] < M) then
                M,jj=chars[j],j
            end
        end

        if jj then
            chars[i],chars[jj]=chars[jj],chars[i]
            local r={}
            for n = i + 1, #chars do 
                r[#r+1] = chars[n]
            end
            table.sort(r)
            local str=table.concat(chars,'',1,i)..table.concat(r)
            if str>word then
                ans=str
                break
            end
            chars[i],chars[jj]=chars[jj],chars[i]
        end
    end
    print(ans or "no answer")
end