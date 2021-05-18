from nicehash import *
import atexit

from apscheduler.schedulers.blocking import BlockingScheduler

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s, %(message)s',
                        handlers=[logging.FileHandler("nicehash_task_scheduler_log.txt"),
                                  logging.StreamHandler()])

    print('Running...') #when code is started, display this in the console
    sched = BlockingScheduler(timezone='US/Eastern') #set up a scheduling object
    sched.add_job(get_public_data_long_term, 'cron', day_of_week=4, hour=10, misfire_grace_time=60 * 5, max_instances=6)  # run the long-term data gethering scripts once a week
    sched.add_job(get_data_1hr, 'cron', minute=11, misfire_grace_time=60 * 5, max_instances=6)  # run the short-term public api hourly
    sched.add_job(get_data_4hr, 'cron', minute=13, hour='1,5,9,13,17,21', misfire_grace_time=60 * 5, max_instances=6)  # run the short-term public api 4-hourly
    sched.add_job(get_data_5mins, 'cron', minute=', '.join([str(i) for i in range(0,56,5)]),  misfire_grace_time=60*5, max_instances=6) #run every 5 mins
    sched.add_job(add_most_recent_rig_device_stats_table, 'cron', minute=', '.join([str(i) for i in range(0,56,5)]),  misfire_grace_time=60*5, max_instances=6) #run every 5 mins
    sched.start() #start the scheduler

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: sched.shutdown())
