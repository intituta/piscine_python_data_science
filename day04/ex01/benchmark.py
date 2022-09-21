# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    benchmark.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/21 16:53:48 by kferterb          #+#    #+#              #
#    Updated: 2022/09/21 16:53:49 by kferterb         ###   ########.fr        #
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
    print(new_list)

def map_approach():
    emails = data()
    m1 = map(lambda email: email if email.find('@gmail.com') != -1 else None, emails)
    # m2 = list(map(lambda email: email if email.find('@gmail.com') != -1 else None, emails))

def compare_time():
    res1 = timeit.timeit('loop_approach()', 
        'from __main__ import loop_approach', number=n)
    res2 = timeit.timeit('comprehension_approach()', 
        'from __main__ import comprehension_approach', number=n)
    res3 = timeit.timeit('map_approach()', 
        'from __main__ import map_approach', number=n)
    if res2 > res1 and res3 > res1:
        print("it is better to use a loop")
        if res2 > res3:
            print(f"{res1} vs {res3} vs {res2}")
        else:
            print(f"{res1} vs {res2} vs {res3}")
    elif res3 > res2 and res1 > res2:
        print("it is better to use a list comprehension")
        if res3 > res1:
            print(f"{res2} vs {res1} vs {res3}")
        else:
            print(f"{res2} vs {res3} vs {res1}")
    elif res2 > res3 and res1 > res3:
        print("it is better to use a map")
        if res1 > res2:
            print(f"{res3} vs {res2} vs {res1}")
        else:
            print(f"{res3} vs {res1} vs {res2}")

if __name__ == '__main__':
    compare_time()
