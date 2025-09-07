-- https://leetcode.com/problems/not-boring-movies/?envType=study-plan-v2&envId=top-sql-50 --

select id, movie, description, rating
from Cinema
where not description = 'boring' and id % 2 != 0
order by rating desc;