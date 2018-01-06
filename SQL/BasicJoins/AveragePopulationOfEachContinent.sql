select continent, floor(avg(c.population))
from city c join country on countrycode = code
group by continent
