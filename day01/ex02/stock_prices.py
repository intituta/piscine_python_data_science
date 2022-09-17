# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stock_prices.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/17 17:18:39 by kferterb          #+#    #+#              #
#    Updated: 2022/09/17 17:18:40 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def data():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    return COMPANIES, STOCKS

def stock_prices():
    if len(sys.argv) != 2:
        return
    
    s = sys.argv[1].capitalize()
    COMPANIES, STOCKS = data()
    if s in COMPANIES:
        print(STOCKS[COMPANIES[s]])
    else:
        print("Unknown company")

if __name__ == '__main__':
    stock_prices()