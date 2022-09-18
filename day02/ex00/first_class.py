# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    first_class.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 12:30:40 by kferterb          #+#    #+#              #
#    Updated: 2022/09/18 14:14:06 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Must_read:
    file = open("data.csv", "r")
    text = file.read()
    print(text)

if __name__ == '__main__':
    pass