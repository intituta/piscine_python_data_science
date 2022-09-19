# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    analytics.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/19 10:09:44 by kferterb          #+#    #+#              #
#    Updated: 2022/09/19 11:27:33 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
from random import randint
import logging
import json
import requests

class Research:
    def __init__(self, path):
        self.path = path
        logging.info("Research class is created")

    def file_reader(self):
        has_header = True
        logging.info('Started reading the file')
        text = self.check_file(has_header)
        return text

    def check_file(self, has_header):
        if not os.access(self.path, os.R_OK):
            raise ValueError("File cannot be read")
        with open(self.path, "r") as f:
            lines = [line.rstrip() for line in f]
        if (len(lines) < 1):
            raise ValueError("Size of the file is too small")
        if lines[0] == "0,1" or lines[0] == "1,0":
            has_header = False
        if has_header and len(lines[0].split(',')) != 2:
            raise ValueError("Header is incorrect")
        mod_lines = []
        if has_header:
            mod_lines = lines[1:]
        else:
            mod_lines = lines
        for line in mod_lines:
            if line != "0,1" and line != "1,0":
                raise ValueError("Data in the file is incorrect")
        res = []
        for line in mod_lines:
            strs = line.split(',')
            numbers = []
            for number in strs:
                numbers.append(int(number))
            res.append(list(numbers))
        logging.debug("File is read and checked")
        return res

    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.info("Calculations class is created")

        def counts(self):
            heads = 0
            tails = 0
            for pair in self.data:
                heads += pair[0]
                tails += pair[1]
            logging.debug("Heads and tails are calculated")
            return heads, tails

        def fractions(self, rand_nums):
            first = rand_nums[0] * 100 / (rand_nums[0] + rand_nums[1])
            second = rand_nums[1] * 100 / (rand_nums[0] + rand_nums[1])
            logging.debug("Fractions of heads and tails are calculated")
            return first, second

    class Analytics(Calculations):
        def predict_random(self, num):
            res = []
            for i in range(num):
                first = randint(0, 1)
                second = 0 if first else 1
                res.append([first, second])
            logging.debug("Random predictions are made")
            return res

        def predict_last(self, res):
            logging.debug("Returning last pair of predictions")
            return res[-1]

        def calc_random(self, res):
            heads = 0
            tails = 0
            for pair in res:
                heads += pair[0]
                tails += pair[1]
            logging.debug("Random heads and tails are calculated")
            return heads, tails

        def save_file(self, data, name_of_file, extension):
            f = open(name_of_file + '.' + extension, "w")
            f.write(data)
            logging.debug("Saving report to the file")
            f.close()

    def send_slack_message(self, payload, webhook):
        return requests.post(webhook, json.dumps(payload))
