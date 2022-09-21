# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    benchmark.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/21 16:53:50 by kferterb          #+#    #+#              #
#    Updated: 2022/09/21 16:53:51 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python

import timeit
import sys

def data():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
                'anna@live.com', 'philipp@gmail.com']
    all_emails = emails * 5
    return all_emails

def loop_approach():
    emails = data()
    new_list = []
    for email in emails:
        if email.find('@gmail.com') != -1:
            new_list.append(email)

def comprehension_approach():
    emails = data()
    new_list = [email for email in emails if email.find('@gmail.com') != -1]

def map_approach():
    emails = data()
    m1 = map(lambda email: email if email.find('@gmail.com') != -1 else None, emails)
    # m2 = list(map(lambda email: email, emails))

def filter_approach():
    emails = data()
    new_list = filter(lambda email: email if email.find('@gmail.com') != -1 else None, emails)

def compare_time(approach, n):
    if approach == 'loop':
        res = timeit.timeit('loop_approach()', 
            'from __main__ import loop_approach', number=n)
    elif approach == 'list_comprehension':
        res = timeit.timeit('comprehension_approach()', 
            'from __main__ import comprehension_approach', number=n)
    elif approach == 'map':
        res = timeit.timeit('map_approach()', 
            'from __main__ import map_approach', number=n)
    elif approach == 'filter':
        res = timeit.timeit('filter_approach()', 
            'from __main__ import filter_approach', number=n)
    else:
        raise ValueError("Approach is invalid")
    print(res)
    
def comp_final():
    if len(sys.argv) != 3:
        raise ValueError("Incorrect number of arguments")
    compare_time(sys.argv[1], int(sys.argv[2]))

if __name__ == '__main__':
    # try:
    #     comp_final()
    # except ValueError as err:
    #     print('\033[91mException!', err)
    comprehension_approach()
