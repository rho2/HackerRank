select * from
(
    select total_earning, count(*)
    from (
        select months*salary as total_earning
        from employee
    )
    group by total_earning
    order by total_earning desc
)
where rownum = 1;