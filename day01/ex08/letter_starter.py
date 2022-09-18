# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    letter_starter.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 10:04:32 by kferterb          #+#    #+#              #
#    Updated: 2022/09/18 10:08:46 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def letter_starter():
    if len(sys.argv) != 2:
        return
    with open("employees.tsv") as f1:
        lines = [line.rstrip() for line in f1]
    res = ""
    for line in lines:
        info = line.split('\t')
        if (sys.argv[1] == info[2]):
            res = "Dear %s, welcome to our team. We are sure that " % info[0]
            res += "it will be a pleasure to work with you. "
            res += "That's a precondition for the professionals that our company hires."
    if not res:
        res = "No such email"
    print(res)

if __name__ == '__main__':
    letter_starter()