#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Product:
    """codstring for Product."""
    id_counter = 0

    def __init__(self, name, recipe = list(), batch_size = 1):
        self.id = Product.id_counter
        Product.id_counter += 1
        self.name = name
        self.recipe = recipe
        self.batch_size = batch_size


class ProductList:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)


class ProductDictionary:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.name] = product.id
    
    def remove_product(self, product):
        del self.products[product.name]
