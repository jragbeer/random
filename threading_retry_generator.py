from pprint import pprint
from multiprocessing import Pool, Process
import datetime
import time
import numpy as np
from itertools import islice

today = datetime.datetime.now()

def do_work(a):
    time.sleep(5)
    b = np.random.randint(1,8)
    if b > 6:
        return (a, "error")
    else:
        return (a, 'good')

def part_one_mp(num = 50, top_ads=True):
    output = []
    additional_time = 0
    values = list(range(num))
    processes=25
    while True:
        pool = Pool(processes=processes)
        workers = [pool.apply_async(do_work, args=(i,)) for i in islice(values, 0, processes)]
        result = [p.get() for p in workers]
        print(f'output of the work is: ')
        pprint(result)
        successes = [(k, v) for k, v in result if v != 'error']
        errors = [(k, v) for k, v in result if v == 'error']
        print(f"{len(errors)} errors: {errors}")
        print(f'checking if all {num} sites are parsed..')
        for t in successes:
            output.append(t)

        if not errors:
            if len(successes) == len(values):
                print("SHOULD BE WEARY")
                break
        # rebuild values and print output information
        values = values[processes:]
        values.extend([k for k,v in errors])
        print(datetime.datetime.now()-today)
        print('values are now: ', values)
        print(f'length of output is {len(output)}')
        print(f'waiting for {additional_time + 1} seconds...')
        # sleep to not be too taxing to website
        time.sleep(additional_time + 6)
        additional_time += 2 # step-algorithm
    pprint(sorted(output))
    return {k: v for k, v in output}
if __name__ == '__main__':
    part_one_mp(100, False)