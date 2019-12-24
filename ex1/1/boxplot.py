#!/usr/bin/python3

import sys
import time
from subprocess import check_output
import csv

if __name__ == '__main__':
    iterations = 10

    with open('phods.csv', mode='w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

        filewriter.writerow(['simple phods', 'opt phods 16x16',
                                            'opt phods 72x2'])

        for i in range(iterations):
            cmd = ['./' + "phods"]
            value = float(check_output(cmd).decode())

            cmd = ['./' + "phods_opt"]
            value_opt = float(check_output(cmd).decode())

            cmd = ['./' + "phods_opt_2dimensions", str(72), str(2)]
            value_opt_2 = float(check_output(cmd).decode())

            filewriter.writerow([value, value_opt, value_opt_2])

    import pandas
    import matplotlib.pyplot as plt
    data = pandas.read_csv('phods.csv', sep=',')
    data.boxplot(column=['simple phods', 'opt phods 16x16', 'opt phods 72x2'])
    plt.show()
