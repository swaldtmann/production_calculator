#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# See https://stackoverflow.com/questions/60218284/find-the-count-of-raw-ingredients-using-recursion-in-python for basic idea!

import json
from collections import defaultdict
import sys

with open('products.json', 'r') as f:
    recipes = json.load(f)

def count_raw_ingredients(recipe):
    ingredients = defaultdict(int)
    for ingredient, amount in recipes[recipe]["ingredients"].items():
        if ingredient not in recipes:
            ingredients[ingredient] += amount
        else:
            bs = recipes[ingredient]["batch_size"]
            for subingredient, subamount in count_raw_ingredients(ingredient).items():
                ingredients[subingredient] += amount * subamount / bs

    return dict(ingredients)

print(count_raw_ingredients('quadruple_axe'), "Batch Size: "+ str(recipes["quadruple_axe"]["batch_size"]))