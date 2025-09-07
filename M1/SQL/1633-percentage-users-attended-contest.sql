-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/?envType=study-plan-v2&envId=top-sql-50 --

cselect r.contest_id,
round(count(r.user_id) * 100.00 / (select count(*) from Users),2) as percentage
from Register r
join Users u
on u.user_id = r.user_id
group by r.contest_id
order by percentage desc, r.contest_id;