from home_data_eng import *
import dagster

@dagster.op
def weather_forecast_func(context,):
    time.sleep(10)
@dagster.op
def weather_historical_canadian_func(context, cereals = None):
    weather_get_historical_data_for_all_can_cities_this_month()
@dagster.op
def clean_hourly_weather_db_func(context, cereals = None):
    fix_empty_rows_weather_historical_hourly_table()
@dagster.op
def weather_historical_intl_func(context):
    weather_get_historical_data_for_all_intl()
@dagster.job
def weather_job():
    clean_hourly_weather_db_func(weather_historical_canadian_func(weather_historical_intl_func()))
    weather_forecast_func()

@dagster.op
def local_pc_stats_func(context,):
    get_pc_stats()

@dagster.job
def pc_stats_job():
    local_pc_stats_func()

weather_job_schedule = dagster.ScheduleDefinition(cron_schedule="0 7 * * *", job=weather_job, execution_timezone="US/Eastern", )
pc_stats_schedule = dagster.ScheduleDefinition(cron_schedule="*/4 * * * *", job=pc_stats_job, execution_timezone="US/Eastern", )

@dagster.repository
def home_repository():
    return [
        weather_job_schedule, weather_job,
        pc_stats_schedule, pc_stats_job
            ]

