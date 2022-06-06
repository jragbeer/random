import logging
import datetime
import time
import traceback
import numpy as np
from functools import wraps
def error_handling():
    """
    This function returns a string with all of the information regarding the error
    :return: string with the error information
    """
    return traceback.format_exc()

def decorator_func(func):
    @wraps(func)
    def inner_func():
        strt_time = datetime.datetime.now()
        result_of_func = None
        try:
            msg = 'SUCCESS'
            end_of_message = ""
            result_of_func = func()
        except:
            msg = 'FAIL'
            end_of_message = error_handling()
        end_time = datetime.datetime.now()
        total_time = strt_time - end_time
        email = f"{msg} | {func.__name__} was completed in {total_time}. {end_of_message}"
        send_email(email)
        logging.info(email)
        return result_of_func

    return inner_func

def send_email(a='a', b='a', c='a'):
    print(f"{a}, {b}, {c}, email sent")

def write_to_log(a=None):
    with open('decorator_test.txt', "a") as f:
        f.write(f"{a} - {datetime.datetime.now()}\n")
    print(a)

@decorator_func
def scheduled_function():
    a = np.random.randint(1, 10)
    if a < 5:
        write_to_log()
        time.sleep(2)
        write_to_log('fun')
        write_to_log('-------------------')
    else:
        raise ValueError

@decorator_func
def scheduled_function2():
    a = np.random.randint(1, 10)
    if a < 5:
        write_to_log(2)
        time.sleep(2)
        write_to_log('fun2')
        write_to_log('-------------------')
    else:
        raise ValueError

