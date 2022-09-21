# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    benchmark.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/21 16:53:55 by kferterb          #+#    #+#              #
#    Updated: 2022/09/21 16:53:56 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python

import timeit
import sys
from functools import reduce

def loop_approach():
    num = int(sys.argv[3])
    sum = 0
    for i in range(1, num + 1):
        sum += i*i

def reduce_approach():
    num = int(sys.argv[3])
    reduce(lambda i, j: i + j*j, range(1, num + 1))

def compare_time(approach, n):
    if approach == 'loop':
        res = timeit.repeat('loop_approach()', 
            'from __main__ import loop_approach', number=n)
    elif approach == 'reduce':
        res = timeit.repeat('reduce_approach()', 
            'from __main__ import reduce_approach', number=n)
    else:
        raise ValueError("Approach is invalid")
    print(sum(res))

def comp_final():
    if len(sys.argv) != 4:
        raise ValueError("Incorrect number of arguments")
    compare_time(sys.argv[1], int(sys.argv[2]))

if __name__ == '__main__':
    try:
        comp_final()
    except ValueError as err:
        print('\033[91mException!', err)
    except TypeError as err:
        print('\033[91mException!', err)