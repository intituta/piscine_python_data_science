# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    benchmark.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/21 16:53:57 by kferterb          #+#    #+#              #
#    Updated: 2022/09/21 16:53:58 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python

import collections
import timeit
import random
from collections import Counter

def random_list():
    random_list = [random.randint(0, 100) for _ in range(1000000)]
    return random_list

def list_to_dict(rand_list):
    keys = [x for x in range(0, 101)]
    values = []
    for k in keys:
        sum = 0
        for r in rand_list:
            if r == k:
                sum += 1
        values.append(sum)
    return dict(zip(keys, values))

def top_ten(rand_list):
    d = list_to_dict(rand_list)
    top10 = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return [x[0] for x in top10][:10]

def counter_dict(rand_list):
    c = collections.Counter(rand_list)
    return c

def counter_top_ten(rand_list):
    c = counter_dict(rand_list)
    top10 = c.most_common(10)
    return [x[0] for x in top10]

def time_res():
    r_list = random_list()
    res1 = timeit.timeit(f'list_to_dict({r_list})',
        'from __main__ import list_to_dict', number=1)
    res2 = timeit.timeit(f'counter_dict({r_list})',
        'from __main__ import counter_dict', number=1)
    res3 = timeit.timeit(f'top_ten({r_list})',
        'from __main__ import top_ten', number=1)
    res4 = timeit.timeit(f'counter_top_ten({r_list})',
        'from __main__ import counter_top_ten', number=1)
    print(f'my function: {res1}\nCounter: {res2}')
    print(f'my top: {res3}\nCounter\'s top: {res4}')

def check_for_me():
    # check 1st part
    my_rand = random_list()
    print(list_to_dict(my_rand))
    print(top_ten(my_rand))
    # check 2nd part
    print(counter_dict(my_rand))
    print(counter_top_ten(my_rand))

if __name__ == '__main__':
    time_res()