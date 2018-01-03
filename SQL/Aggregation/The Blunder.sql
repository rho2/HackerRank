select ceil(avg(salary) - avg(s))
from (
        select salary, replace(salary, '0') as s
        from EMPLOYEES
    );
