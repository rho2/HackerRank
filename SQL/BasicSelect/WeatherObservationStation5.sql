select distinct city, length(city)
from station
order by length(city), city
limit 1;

select distinct city, length(city)
from station
order by length(city) desc, city asc
limit 1;