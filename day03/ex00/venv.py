# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    venv.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/19 12:43:08 by kferterb          #+#    #+#              #
#    Updated: 2022/09/20 14:00:32 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python

import os

def print_virtual_env():
    print("Your current virtual env is " + os.environ['VIRTUAL_ENV'])

if __name__ == '__main__':
    print_virtual_env()
