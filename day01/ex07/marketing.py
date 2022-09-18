# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    marketing.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 10:00:22 by kferterb          #+#    #+#              #
#    Updated: 2022/09/18 10:00:23 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def data():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
                'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                    'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return clients, participants, recipients

def call_center():
    clients, participants, recipients = data()
    return list(set(clients) - set(recipients))

def potential_clients():
    clients, participants, recipients = data()
    return list(set(participants) - set(clients))

def loyalty_program():
    clients, participants, recipients = data()
    return list(set(clients) - set(participants))

def marketing():
    if len(sys.argv) != 2:
        return
    if (sys.argv[1] == 'call_center'):
        print(call_center())
    elif (sys.argv[1] == 'potential_clients'):
        print(potential_clients())
    elif (sys.argv[1] == 'loyalty_program'):
        print(loyalty_program())
    else:
       raise ValueError('Wrong name is given') 

if __name__ == '__main__':
    marketing()