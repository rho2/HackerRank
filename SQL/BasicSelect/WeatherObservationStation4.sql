select count(*)  - (
    select count(*) from (
        select distinct city
        from station 
    ) as tmp
) as gcnt
from station;