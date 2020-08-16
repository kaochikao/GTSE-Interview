



-- RS, running total
select
    log_id,
    count(log_id) over (order by log_id rows unbounded preceding ) as running_total
from gtse.Logs