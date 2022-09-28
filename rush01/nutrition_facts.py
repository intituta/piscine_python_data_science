#!/usr/bin/env python3.9 -B

import pandas as pd
import numpy as np
import requests

class NutritionFacts:
    """
    Offering nutritional facts on given ingredients.
    """
    def __init__(self, list_of_ingredients):
        self.list_of_ingredients = list_of_ingredients
        self.check_args()
        self.daily_portion = self.daily_amount()
        self.api_key = 'SmPYB4v9WYhjeLd9zHtDCstEhi11uy9iJ2Vg2ha6'
        self.nuts = self.get_nutrition_info()
        self.res = self.retrieve()

    def get_nutrition_info(self):
        nuts = {}
        for ingredient in self.list_of_ingredients:
            before = ingredient
            ingr = ingredient.split(' ')
            if len(ingr) != 1:
                ingredient = ''
                for i in range(len(ingr)):
                    ingredient += ingr[i]
                    if i != len(ingr) - 1:
                        ingredient += '%'
            url = f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query={ingredient}'
            session = requests.Session()
            session.headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.607 Yowser/2.5 Safari/537.36'}
            page = session.get(
                    url,
                    timeout=(60,60),
                    stream=True, proxies = {"http": "http://85.195.104.71:80"},
                    auth=(self.api_key, '')
                )
            info = page.json()
            nutrients = info['foods'][0]['foodNutrients']
            nutr_info = {}
            for nutrient in nutrients:
                nutr_info[nutrient['nutrientName']] = [nutrient['value'], nutrient['unitName']]
            nuts[before] = nutr_info
        return nuts

    def daily_amount(self):
        daily_reference = pd.read_csv('data/daily_reference.csv')
        daily_portion = {}
        for k, v in daily_reference.set_index('Nutrient').T.to_dict('list').items():
            daily_portion[k] = v[1]
        return daily_portion

    def retrieve(self):
        res = {}
        for kn, vn in self.nuts.items():
            res_nutr = {}
            for kv,vv in vn.items():
                for key, value in self.daily_portion.items():
                    if kv.lower().find(key.lower()) != -1:
                        if key not in res_nutr and vv[0] != 0:
                            res_val = 1 / value
                            if vv[1] == 'MG':
                                res_val /= 10 ** 3
                            elif vv[1] == 'UG':
                                res_val /= 10 ** 6
                            elif vv[1] == 'IU' and key.find('Vitamin D') != -1:
                                res_val = res_val * 0.6 / 10 ** 6
                            elif vv[1] == 'IU':
                                res_val = res_val * 25 / 10 ** 9
                            res_val *= vv[0]
                            res_nutr[key] = res_val
            res[kn] = res_nutr
        return res

    def print_nutrition(self):
        print('\nII. NUTRITION FACTS')
        for k,v in self.res.items():
            print(k.capitalize())
            for name, part in v.items():
                print(f'{name} - {part:.0%} of Daily Value')
            print('')

    def check_args(self):
        all_ingredients = np.loadtxt('data/ingr.csv', dtype='object', delimiter=',')
        for ingr in self.list_of_ingredients:
            flag = False
            for all_ingr in all_ingredients:
                if ingr == all_ingr:
                    flag = True
                    break
            if flag == False:
                raise ValueError('No such ingredient')
    

    def filter(self, n):
        sorted_facts = {}
        for k,v in self.res.items():
            sorted_facts[k] = {k: v for k, v in sorted(v.items(), key=lambda item: item[1])}
        text_with_facts = dict(list(sorted_facts.items())[:n])
        return text_with_facts


ingridients = ['yogurt', 'bean']
myclass = NutritionFacts(ingridients)
text_with_facts = myclass.filter(5)
for k,v in text_with_facts.items():
    print(k,v)
# myclass.print_nutrition()