#!/usr/bin/env python

from time import sleep
from bs4 import BeautifulSoup
import httpx
import sys

import cProfile
import pstats

def check_args():
    if len(sys.argv) != 3:
        raise ValueError("No input")
    ar1 = sys.argv[1].lower()
    ar2 = sys.argv[2]
    return ar1, ar2

def connect_to_server(ar1):
    url = f'https://finance.yahoo.com/quote/{ar1}/financials?p={ar1}'
    page = httpx.get(url, headers={'User-Agent': 'Custom'})
    if page.status_code != 200:
        raise ValueError("URL doesn't exist")
    return page

def page_parser(page, ar1, ar2):
    soup = BeautifulSoup(page.text, "html.parser")
    value = soup.find_all('div', class_ = 'D(tbr) fi-row Bgc($hoverBgColor):h')
    res = []
    for val in value:
        if (val.span.text == ar2):
            res.append(val.span.text)
            nums1 = val.find_all('div', class_ = 'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')
            nums2 = val.find_all('div', class_ = 'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)')
            for num in nums1 + nums2:
                res.append(num.span.text)
    if not res:
        raise ValueError(f"Field {ar2} in {ar1} doesn't exist")
    return tuple(res)

def result():
    try:
        ar1, ar2 = check_args()
        page = connect_to_server(ar1)
        result = page_parser(page, ar1, ar2)
        print(result)
    except ValueError as exp:
        print('\033[91mException!', exp)
    # sleep(5)

if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()
    result()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats(5)

# compile with cProfile, pstats
#!/usr/bin/env python -m cProfile -s tottime
#!/usr/bin/env python -m cProfile -s calls