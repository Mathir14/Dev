-- https://leetcode.com/problems/customers-who-bought-all-products/description/?envType=study-plan-v2&envId=top-sql-50 --

select c.customer_id
from Customer c
inner join Product p
on c.product_key = p.product_key
group by c.customer_id
having count(distinct c.product_key) = (select count(*) from Product);