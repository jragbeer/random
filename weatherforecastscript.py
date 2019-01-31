from weatherscripts import *

logging.basicConfig(level=logging.INFO, format = '%(asctime)s,%(message)s',
                    handlers=[logging.FileHandler("weather_forecast_log.txt"),
                              logging.StreamHandler()])

print('Running...') #when code is started, display this in the console
sched = BlockingScheduler() #set up a scheduling object
sched.add_job(gather_weather_forecasts, 'cron', minute=30) #run the weather forecast ingest every half an hour
sched.start() #start the scheduler
