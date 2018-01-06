select c.name
from city c join country on countrycode = code
where continent = "Africa"