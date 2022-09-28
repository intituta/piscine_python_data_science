#!/usr/bin/env python3.9 -B -W ignore

from nutrition_facts import NutritionFacts
from forecast import Forecast
import sys

def return_ingr():
    res = []
    if len(sys.argv) < 2:
        raise ValueError('No input')
    for i in range(1, len(sys.argv)):
        if i != len(sys.argv) - 1 and len(sys.argv) > 2:
            res.append(sys.argv[i][:-1])
        else:
            res.append(sys.argv[i])
    return res

if __name__ == '__main__':
    try:
        list_of_ingredients = return_ingr()
        f = Forecast(list_of_ingredients)
        f.preprocess()
        print('I. OUR FORECAST')
        print(f.predict_rating())
        # myclass = NutritionFacts(list_of_ingredients)
        # myclass.print_nutrition()
    except ValueError as err:
        print('Exception!', err)
    except KeyError:
        print('Please wait for the answer from the server')
