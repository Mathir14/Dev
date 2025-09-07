-- https://leetcode.com/problems/product-sales-analysis-iii/description/?envType=study-plan-v2&envId=top-sql-50 --
select s1.product_id, s1.year as first_year, s1.quantity, s1.price
from Sales s1
join(
    select product_id, min(year) as min_year
    from Sales
    group by product_id
) s2
on s1.product_id = s2.product_id
and s1.year = s2.min_year;