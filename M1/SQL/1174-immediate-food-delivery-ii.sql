-- https://leetcode.com/problems/immediate-food-delivery-ii/description/?envType=study-plan-v2&envId=top-sql-50 --

select 
round(sum(case when order_date = customer_pref_delivery_date then 1.0 else 0.0 end) * 100.00 / count(*),2) as immediate_percentage
from Delivery
where (customer_id , order_date) in(
select customer_id, min(order_date)
from Delivery
group by customer_id);