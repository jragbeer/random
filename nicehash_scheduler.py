from nicehash import *
import dagster

# SOLIDS / TASKS

@dagster.solid
def five_min_func():
    get_data_5mins()

@dagster.solid
def long_term_nicehash_public():
    get_public_data_long_term()

@dagster.solid
def four_hour_func():
    get_data_4hr()

@dagster.solid
def one_hour_func():
    get_data_1hr()

@dagster.solid
def make_easy_sql_func(context, cereals=None):
    add_most_recent_rig_device_stats_table()

# PIPELINES

@dagster.pipeline
def one_hour_pipeline():
    one_hour_func()

@dagster.pipeline
def four_hour_pipeline():
    four_hour_func()

@dagster.pipeline
def five_min_pipeline():
    make_easy_sql_func(five_min_func())

@dagster.pipeline
def long_term_pipeline():
    long_term_nicehash_public()

# SET SCHEDULES FOR EACH PIPELINE

@dagster.schedule(cron_schedule="0 10 * * 4", pipeline_name="long_term_pipeline", execution_timezone="US/Eastern")
def nicehash_longterm_scheduler(_context):
    pass

@dagster.schedule(cron_schedule="0 */4 * * *", pipeline_name="four_hour_pipeline", execution_timezone="US/Eastern")
def nicehash_4hr_scheduler(_context):
    pass

@dagster.schedule(cron_schedule="0 */1 * * *", pipeline_name="one_hour_pipeline", execution_timezone="US/Eastern")
def nicehash_1hr_scheduler(_context):
    pass

@dagster.schedule(cron_schedule="*/5 * * * *", pipeline_name="five_min_pipeline", execution_timezone="US/Eastern")
def nicehash_5min_scheduler(_context):
    pass

# WHATS IS VISIBLE IN REPOSITORY

@dagster.repository
def nicehash_repository():
    return [one_hour_pipeline, four_hour_pipeline, five_min_pipeline, long_term_pipeline, nicehash_longterm_scheduler, nicehash_1hr_scheduler,nicehash_4hr_scheduler,nicehash_5min_scheduler]
