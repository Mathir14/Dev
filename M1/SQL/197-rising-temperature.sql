-- https://leetcode.com/problems/rising-temperature/description/ --

select curr.id
from Weather curr
join Weather prev
on curr.recordDate = prev.recordDate + interval '1 day'
where curr.temperature > prev.temperature;