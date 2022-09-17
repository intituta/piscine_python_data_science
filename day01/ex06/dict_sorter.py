# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dict_sorter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/17 17:18:53 by kferterb          #+#    #+#              #
#    Updated: 2022/09/17 17:38:19 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def data():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    return list_of_tuples

def get_key(my_dict, val):
    for key, value in my_dict.items():
         if val == value:
             return key

def to_dictionary(list_of_tuples):
    my_dict = dict(list_of_tuples)
    return my_dict

def value_to_int(my_dict):
    new_dict = {}
    for k, v in my_dict.items():
        new_dict[k] = int(v)
    return new_dict

def sort_dict_by_v(x):
    sorted_dict = {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}
    return sorted_dict

def check_equals(x):
    new_dict = {}
    k = list(x.keys())
    v = list(x.values())
    for i in range(len(k) - 1):
        if (v[i] == v[i + 1]):
            if k[i + 1] < k[i]:
                k[i], k[i + 1] = k[i + 1], k[i]
    new_dict = dict(zip(k, v))
    return new_dict

# for check
def print_dict(my_dict):
    for key, value in my_dict.items():
        print("\'%s\' : \'%d\'" % (key, value))

def print_final():
    my_dict = to_dictionary(data())
    my_dict = value_to_int(my_dict)
    sorted_dict = sort_dict_by_v(my_dict)
    sorted_dict = check_equals(sorted_dict)
    for key in sorted_dict.keys():
        print(key)
    # for check
    # print("------------")
    # print_dict(sorted_dict)

if __name__ == '__main__':
    print_final()