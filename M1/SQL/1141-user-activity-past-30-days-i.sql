-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/?envType=study-plan-v2&envId=top-sql-50 --

select activity_date as day,
count(distinct user_id) as active_users
from Activity
where activity_date between ('2019-07-27'::date - interval '29 day') and '2019-07-27'
group by activity_date;