from nicehash import *
import dagster

# OPS / TASKS

@dagster.op
def five_min_func():
    get_data_5mins()

@dagster.op
def check_running():
    are_gpus_runnning()

@dagster.op
def long_term_nicehash_public():
    get_public_data_long_term()

@dagster.op
def four_hour_func():
    get_data_4hr()

@dagster.op
def one_hour_func():
    get_data_1hr()

@dagster.op
def make_easy_sql_func(context, cereals=None):
    add_most_recent_rig_device_stats_table()

# JOBS

@dagster.job
def one_hour_job():
    one_hour_func()
    check_running()

@dagster.job
def four_hour_job():
    four_hour_func()

@dagster.job
def five_min_job():
    make_easy_sql_func(five_min_func())

@dagster.job
def long_term_job():
    long_term_nicehash_public()

# SET SCHEDULES FOR EACH JOB

nicehash_longterm_schedule = dagster.ScheduleDefinition(cron_schedule="0 10 * * 4", job=long_term_job, execution_timezone="US/Eastern", )

nicehash_4hr_schedule = dagster.ScheduleDefinition(cron_schedule="0 */4 * * *", job=four_hour_job, execution_timezone="US/Eastern", )

nicehash_1hr_schedule = dagster.ScheduleDefinition(cron_schedule="0 */1 * * *", job=one_hour_job, execution_timezone="US/Eastern", )

nicehash_5min_schedule = dagster.ScheduleDefinition(cron_schedule="*/5 * * * *", job=five_min_job, execution_timezone="US/Eastern", )

# WHATS IS VISIBLE IN REPOSITORY
@dagster.repository
def nicehash_repository():
    return [one_hour_job, four_hour_job, five_min_job, long_term_job, nicehash_longterm_schedule, nicehash_1hr_schedule, nicehash_4hr_schedule, nicehash_5min_schedule]
