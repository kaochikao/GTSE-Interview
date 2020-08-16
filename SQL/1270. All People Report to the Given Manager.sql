
-- sub-query法

with d1 as(
    select employee_id from Employees where manager_id = 1 and not employee_id = 1
),
d2 as (
    select employee_id from Employees where manager_id in (select employee_id from d1)
),
d3 as (
    select employee_id from Employees where manager_id in (select employee_id from d2)
)
select employee_id from d1
union all
select employee_id from d2
union all
select employee_id from d3


-- JOIN法
select base.employee_id 
from Employees base
join Employees d1 on base.manager_id = d1.employee_id
join Employees d2 on d1.manager_id = d2.employee_id
join Employees d3 on d2.manager_id = d3.employee_id
where not base.employee_id = 1
and d3.employee_id = 1


