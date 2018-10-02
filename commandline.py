import os
import glob
import sys
import subprocess
import shutil
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

path = r'C:/Users/J_Ragbeer/Desktop/xx/'
all_orig_files = glob.glob(os.path.join(path, "*"))

def run():
    global all_orig_files
    all_files = glob.glob(os.path.join(path, "*"))
    new_files = [x for x in all_files if x not in all_orig_files]
    print(new_files)
    d = os.path.join("C:\\Users\\J_Ragbeer\\Downloads\\xx")
    if not os.path.exists(d):
        os.makedirs(d)
    for f in new_files:
        shutil.copy2(f, d)
    print('Copy done at {}'.format(datetime.datetime.now()))
    all_orig_files = glob.glob(os.path.join(path, "*"))

print('Running...') #when code is started, display this in the console
print('ORIGINAL FILES IN DIRECTORY: \n')
print(all_orig_files)

sched = BlockingScheduler() #set up a scheduling object

sched.add_job(run, 'interval', minutes=5) #run the ping code every hour at 5 minutes
sched.start() #start the scheduler


