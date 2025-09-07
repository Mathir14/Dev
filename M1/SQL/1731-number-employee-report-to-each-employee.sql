-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/?envType=study-plan-v2&envId=top-sql-50 --

select e1.employee_id, e1.name, e2.reports_count, e2.average_age
from Employees e1
join (
    select reports_to, count(*) as reports_count,
    round(avg(age)) as average_age
    from employees
    where reports_to is not null
    group by reports_to
) e2
on e1.employee_id = e2.reports_to
order by e1.employee_id;
    