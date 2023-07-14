#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# See https://stackoverflow.com/questions/60218284/find-the-count-of-raw-ingredients-using-recursion-in-python for basic idea!

import json
from collections import defaultdict
import sys
import math

with open('products.json', 'r') as f:
    recipes = json.load(f)

def count_raw_ingredients(recipe, to_level=0, bom_level=1):
    ingredients = defaultdict(int)
    for ingredient, amount in recipes[recipe]["ingredients"].items():
        if ingredient not in recipes:
            ingredients[ingredient] += amount
        else:
            #print(bom_level)
            if to_level:
                if to_level >= bom_level:
                    ingredients[ingredient] += amount
                    print(ingredient)
                    continue
            bs = recipes[ingredient]["batch_size"]
            for subingredient, subamount in count_raw_ingredients(ingredient, bom_level=bom_level+1).items():
                ingredients[subingredient] += amount * subamount / bs

    return dict(ingredients)

#for product in ["Large Optronic Bridge", "Large Optronic Matrix"]: #  56 / 20
print(count_raw_ingredients("Small Optronic Bridge"), "Batch Size: "+ str(recipes["Small Optronic Bridge"]["batch_size"]))

#sys.exit()

products = defaultdict(int)
#products["Large Optronic Bridge"] = 56
#products["Large Optronic Matrix"] = 20
products["Small Optronic Bridge"] = 16


total_ingredients = defaultdict(int)

for product, amount in products.items():
    print(f"{amount} x {product}:")
    for ing, am in sorted(count_raw_ingredients(product).items()):
        total_ingredients[ing] += am*amount
        print(f"{math.ceil(am*amount):6.0f} x {ing}")

print("Total:")
for ing2, am2 in sorted(total_ingredients.items()):
    print(f"{math.ceil(total_ingredients[ing2]):6.0f} x {ing2}")
