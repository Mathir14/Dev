-- https://leetcode.com/problems/primary-department-for-each-employee/description/?envType=study-plan-v2&envId=top-sql-50 --

select employee_id, department_id
from Employee
where primary_flag = 'Y'

union

select e1.employee_id, e1.department_id
from Employee e1
join(
    select employee_id
    from Employee
    group by employee_id
    having count(department_id) = 1
) e2
on e1.employee_id = e2.employee_id;