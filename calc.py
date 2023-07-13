#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from collections import defaultdict
import sys

with open('recipes.json', 'r') as f:
    recipes = json.load(f)

raw_ingredients = recipes["raw_ingredients"]
del recipes["raw_ingredients"]

#print(recipes)
#print(raw_ingredients)

#sys.exit()

def count_raw_ingredients(recipe):
    ingredients = defaultdict(int)

    for ingredient, amount in recipes[recipe].items():
        if ingredient == "batch_size":
            continue
        if ingredient in raw_ingredients:
            ingredients[ingredient] += amount
        else:
            for subingredient, subamount in count_raw_ingredients(ingredient).items():
                ingredients[subingredient] += amount * subamount

    return dict(ingredients)

print(count_raw_ingredients('quadruple_axe'), "Batch Size: "+ str(recipes["quadruple_axe"]["batch_size"]))