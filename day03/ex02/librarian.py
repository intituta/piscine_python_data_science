# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    librarian.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/19 18:13:54 by kferterb          #+#    #+#              #
#    Updated: 2022/09/19 18:20:51 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python

import os


if __name__ == '__main__':
    print(os.environ['VIRTUAL_ENV'])
    try:
        if not os.environ['VIRTUAL_ENV'].endswith('kferterb'):
            raise Exception('Incorrect env')
    except Exception as ex:
        print(ex)
    else:
        os.system('pip install beautifulsoup4 PyTest')
        os.system('pip freeze > requirements.txt')