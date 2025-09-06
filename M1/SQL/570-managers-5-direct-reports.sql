-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/ --

select E1.name
from Employee e1
join Employee e2
on e1.id = e2.managerId
group by e1.name, e1.id
having count(e2.managerId) >= 5;