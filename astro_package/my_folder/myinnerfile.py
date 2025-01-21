

# import sys

# print(sys.path)

# sys.path.insert(0,"/home/nitinkeshav/astro/")

from astro_package.myouterfile import constant as c

print(c) 

import json
from pathlib import Path

import numpy as np

print(np.__version__)

this_dir=Path(__file__).parent

def check_city(city):
    
    city = city.lower()
    
    with open(f'{this_dir}/city.json') as f:
        data = json.load(f)
        
    #
    #print(data)    
    if city == data['city'].lower():
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(check_city('bangalore'))
    print(check_city('New York'))
