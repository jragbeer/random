from decorator_practice import *
import atexit
from apscheduler.schedulers.blocking import BlockingScheduler

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s, %(message)s',
                        handlers=[logging.FileHandler("decorator.log"),
                                  logging.StreamHandler()])

    print('Running...') #when code is started, display this in the console
    sched = BlockingScheduler(timezone='US/Eastern') #set up a scheduling object
    sched.add_job(scheduled_function, 'interval', minutes=2, misfire_grace_time=60*5, max_instances=6) #run the weather forecast ingest every half an hour
    sched.start() #start the scheduler

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: sched.shutdown())
