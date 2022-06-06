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

def decorator_function(func):
    """
    This function takes in a function as an argument. It runs that function and if successful,
    puts a success note in the log and sends a success email. If it fails, it will put a failure note
    in the log and send a failure email. Timings of how long the execution takes are also done.

    :param func: the function you want wrapped in the special code.
    :return: the result of the inner function
    """
    # this next line treats inner_func like the input function, so that the scheduler names it properly in the log.
    @wraps(func)
    def inner_func():
        """
        Inner function that wraps the input function
        :return: the result of the input function, or None
        """
        strt_time = datetime.datetime.now()
        result_of_func = None  # default value for the result
        try:
            msg = 'SUCCESS'
            end_of_message = ""
            result_of_func = func()
        except:
            msg = 'FAIL'
            end_of_message = error_handling()  # traceback of the error as a string
        end_time = datetime.datetime.now()
        total_time = end_time - strt_time  # total execution time of the process
        email = f"{msg} | {func.__name__} was completed in {total_time}. {end_of_message}"
        # send an email and log this message
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

@decorator_function
def scheduled_function():
    a = np.random.randint(1, 10)
    if a < 5:
        write_to_log()
        time.sleep(2)
        write_to_log('fun')
        write_to_log('-------------------')
    else:
        raise ValueError

@decorator_function
def scheduled_function2():
    a = np.random.randint(1, 10)
    if a < 5:
        write_to_log(2)
        time.sleep(2)
        write_to_log('fun2')
        write_to_log('-------------------')
    else:
        raise ValueError

