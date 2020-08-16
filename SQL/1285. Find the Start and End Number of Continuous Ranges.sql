

with tmp as (
    select 
        log_id,
        -- 人工row_id, 這裡有無加partition by 有什麼差，要實驗
        count(log_id) over (order by log_id) as row_id
    from Logs
), tmp2 as (
    select 
        log_id,
        log_id - row_id as diff
    from tmp
)
select 
min(log_id) as start_id,
max(log_id) as end_id
from tmp2
group by diff


-- MS SQL用 row_number() over (order by log_id)

-- 炫技練習，半對，沒差，就練習
with a as (
    select 
        log_id,
        lag(log_id, 1) over(order by log_id) as prev_row,
        lead(log_id, 1) over(order by log_id) as next_row
    from Logs
), b as (
    select 
        log_id,
        case 
            when (log_id - prev_row) = 1 then
                case
                    when (log_id - next_row) = -1 then 'mid'
                    else 'end'
                end
            else 'start'
        end as row_type
    from a
), c_start as (
    select 
        log_id,
        row_number() over (order by log_id) as row_id
    from b
    where row_type = 'start'
), c_end as (
    select
        log_id,
        row_number() over (order by log_id) as row_id
    from b
    where row_type = 'end'
)

select 
    s.log_id as start_id,
    isnull(e.log_id, s.log_id) as end_id
    -- e.log_id as end_id
from c_start s
-- 這裡有個edge case, 10沒有end, 用inner join就會有錯
left outer join c_end e
on s.row_id = e.row_id


