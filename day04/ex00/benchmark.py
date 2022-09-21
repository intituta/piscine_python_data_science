# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    benchmark.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/21 16:53:45 by kferterb          #+#    #+#              #
#    Updated: 2022/09/21 16:53:46 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python

import timeit

n = 900000
# 90000000

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

def compare_time():
    res1 = timeit.timeit('loop_approach()', 
        'from __main__ import loop_approach', number=n)
    res2 = timeit.timeit('comprehension_approach()', 
        'from __main__ import comprehension_approach', number=n)
    if res1 > res2:
        print("it is better to use a list comprehension")
        print(f"{res2} vs {res1}")
    else:
        print("it is better to use a loop")
        print(f"{res1} vs {res2}")

if __name__ == '__main__':
    compare_time()
