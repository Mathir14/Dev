-- https://leetcode.com/problems/game-play-analysis-iv/description/?envType=study-plan-v2&envId=top-sql-50 --

select
    round(count(distinct first_logins.player_id) * 1.0 / (select count(distinct player_id) from Activity),2) as fraction
from (select player_id, min(event_date) as first_login
    from Activity 
    group by player_id) first_logins
join Activity next_login
on first_logins.player_id = next_login.player_id
and next_login.event_date = first_logins.first_login + interval '1 day';