# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    read_and_write.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/17 10:47:41 by kferterb          #+#    #+#              #
#    Updated: 2022/09/17 10:47:42 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def read_and_write(file):
    f1 = open(file, "r")
    text = f1.read() \
            .replace("\",", "\"\t") \
            .replace(",\"", "\t\"") \
            .replace("true,", "true\t") \
            .replace("false,", "false\t")
    f2 = open("ds.tsv", "w")
    f2.write(text)
    f1.close()
    f2.close()

if __name__ == '__main__':
    read_and_write("ds.csv")