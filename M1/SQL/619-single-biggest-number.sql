-- https://leetcode.com/problems/biggest-single-number/description/?envType=study-plan-v2&envId=top-sql-50 --

select max(num) as num
from (select num
from MyNumbers
group by num
having count(num) = 1);