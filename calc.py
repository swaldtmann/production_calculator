#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# See https://stackoverflow.com/questions/60218284/find-the-count-of-raw-ingredients-using-recursion-in-python for basic idea!

import json
from collections import defaultdict
import sys
import math

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

#for product in ["Large Optronic Bridge", "Large Optronic Matrix"]: #  56 / 20
#    print(count_raw_ingredients(product), "Batch Size: "+ str(recipes[product]["batch_size"]))

total_ingredients = defaultdict(int)
print("Full set of CPU Extenders needs:")
bridge_name = "Large Optronic Bridge"
brigde_count = 56
print(f"{brigde_count} x {bridge_name}:")
for ing, am in sorted(count_raw_ingredients(bridge_name).items()):
    total_ingredients[ing] += am*brigde_count
    print(f"{math.ceil(total_ingredients[ing]):6.0f} x {ing}")
matrix_name = "Large Optronic Matrix"
matrix_count = 20
print(f"{matrix_count} x {matrix_name}:")
for ing1, am1 in sorted(count_raw_ingredients(matrix_name).items()):
    total_ingredients[ing1] += am1*matrix_count
    print(f"{math.ceil(am1*matrix_count):6.0f} x {ing1}")
print("Total:")
for ing2, am2 in sorted(total_ingredients.items()):
    print(f"{math.ceil(total_ingredients[ing2]):6.0f} x {ing2}")
