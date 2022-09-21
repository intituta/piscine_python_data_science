# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/21 16:54:01 by kferterb          #+#    #+#              #
#    Updated: 2022/09/21 16:54:02 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python

import sys
import os
import psutil

def generator(file):
    for line in open(file, "r"):
        yield line

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError("Wrong number of arguments")
        for line in generator(sys.argv[1]):
            pass
        process = psutil.Process(os.getpid())
        print(f'Peak memory usage = {process.memory_info().rss / 1024 ** 3:0.3f} GB')
        cpu_times = process.cpu_times()
        print(f'User Mode Time + System Mode Time = {cpu_times.user + cpu_times.system:0.2f}s')
    except ValueError as err:
        print('\033[91mException!', err)
    except FileNotFoundError as err:
        print('\033[91mException!', err)

# /goinfre/agidget/day04/ratings.csv