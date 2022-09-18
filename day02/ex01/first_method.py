# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    first_method.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 14:04:42 by kferterb          #+#    #+#              #
#    Updated: 2022/09/18 14:05:24 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Research:
    def file_reader(self):
        file = open("data.csv", "r")
        text = file.read()
        return text

if __name__ == '__main__':
    m = Research()
    print(m.file_reader())