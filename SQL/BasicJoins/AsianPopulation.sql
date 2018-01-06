select sum(c.population)
from city c join country on countrycode = code
where continent = "Asia"