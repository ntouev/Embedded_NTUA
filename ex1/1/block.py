#!/usr/bin/python3

import sys
from subprocess import check_output

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 block.py phods_opt/phods_opt_2dimensions [iterations]")
        raise SystemExit

    if sys.argv[1] == 'phods_opt':
        block_sizes = [1, 2, 4, 8, 16]
        for N in block_sizes:
            cmd = ['./' + sys.argv[1], str(N)]
            iterations = int(sys.argv[2])

            suma = 0
            for i in range(iterations):
                value = float(check_output(cmd).decode())
                #print('./', sys.argv[1], sys.argv[2], '--> Value', i, ':', value)
                suma += value

            avg = suma/iterations
            print('Block size', N, ':', str.format('{0:.6f}', avg), 'sec')
            
    elif sys.argv[1] == 'phods_opt_2dimensions':
        N = 144
        M = 176
        min = 1
        bx = 1
        by = 1

        for bx in range (1,N+1,1):
            if N%bx == 0:
                for by in range (1,M+1,1):
                    if M%by == 0:
                        cmd = ['./' + sys.argv[1], str(bx), str(by)]
                        iterations = int(sys.argv[2])

                        suma = 0
                        for i in range(iterations):
                            value = float(check_output(cmd).decode())
                            suma += value

                        avg = suma/iterations
                        print('Block size', bx,'x',by,':', str.format('{0:.6f}', avg), 'sec')

                    if avg < min:
                        min = avg
                        bx_min = bx
                        by_min = by

        print('Best block size:', bx_min, 'x', by_min, ':', str.format('{0:.6f}', min), 'sec')

    else:
        print("Usage: python3 block.py phods_opt/phods_opt_2dimensions [iterations]")
        raise SystemExit
