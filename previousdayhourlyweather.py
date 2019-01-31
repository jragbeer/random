from weatherscripts import *

logging.basicConfig(level=logging.INFO, format = '%(asctime)s,%(message)s',
                    handlers=[logging.FileHandler("previous_day_weather_daily_log.txt"),
                              logging.StreamHandler()])

print('Running...') #when code is started, display this in the console
sched = BlockingScheduler() #set up a scheduling object
sched.add_job(gather_previous_day_weather_daily, 'cron', hour=9) #run the weather ingest every morning at 9am
sched.start() #start the scheduler