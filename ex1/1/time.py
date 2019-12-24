#!/usr/bin/python3

import sys
import time
from subprocess import check_output

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: time.py [phods/phods_opt] [iterations]")
        raise SystemExit

    cmd = ['./' + sys.argv[1]]
    iterations = int(sys.argv[2])

    suma = 0
    min = 1
    max = 0

    for i in range(iterations):
        value = float(check_output(cmd).decode())

        #print('Value', i, ':', value)
        suma += value
        if value < min:
            min = value
        if value > max:
            max = value

    avg = suma/iterations

    print('Min: ', min, 'sec')
    print('Max: ', max, 'sec')
    print('Average: ', str.format('{0:.6f}', avg), 'sec')
