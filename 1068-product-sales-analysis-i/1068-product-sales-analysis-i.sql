# Write your MySQL query statement below
select prod.product_name, sal.year, sal.price
from Sales sal
left join Product prod
on sal.product_id = prod.product_id;