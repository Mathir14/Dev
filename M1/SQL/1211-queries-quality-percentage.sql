-- https://leetcode.com/problems/queries-quality-and-percentage/description/?envType=study-plan-v2&envId=top-sql-50 --

select query_name,
round(avg(rating * 1.0 / position),2) as quality,
round(sum(case when rating < 3 then 1.00 else 0.00 end) * 100.00 / count(*) , 2) as poor_query_percentage
from Queries
group by query_name;