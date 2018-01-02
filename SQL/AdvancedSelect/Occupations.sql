with d (i, d_name)as (
        select rownum, name
        from (select * 
              from occupations
              where occupation = 'Doctor'
              order by name)),
    p (i, p_name)as (
        select rownum, name
        from (select * 
              from occupations
              where occupation = 'Professor'
              order by name)),
    s (i, s_name)as (
        select rownum, name
        from (select * 
              from occupations
              where occupation = 'Singer'
              order by name)),
    a (i, a_name)as (
        select rownum, name
        from (select * 
              from occupations
              where occupation = 'Actor'
              order by name))
select d_name, p_name, s_name, a_name
from d 
    full outer join p on d.i = p.i
    full outer join s on p.i = s.i
    full outer join a on s.i = a.i;