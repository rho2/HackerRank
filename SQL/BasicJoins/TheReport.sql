select (
    case g.grade>=8 
    when true then s.name 
    else null end),g.grade,s.marks 
from students s inner join grades g 
    on s.marks >= min_mark 
    AND s.marks <= max_mark 
order by g.grade desc,s.name,s.marks;