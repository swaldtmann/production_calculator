#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BillOfMaterials:
    def __init__(self, name, quantity, components=None):
        self.name = name
        self.quantity = quantity
        self.components = components if components is not None else []

    def add_component(self, component):
        self.components.append(component)

    def print_bom(self, level=0):
        indent = "    " * level
        print(f"{indent}{self.name} - {self.quantity}")
        for component in self.components:
            component.print_bom(level + 1)


if __name__ == "__main__":
        # Create the top-level component
    top_component = BillOfMaterials("Product A", 1)

    # Create sub-components
    sub_component_1 = BillOfMaterials("Component X", 2)
    sub_component_2 = BillOfMaterials("Component Y", 3)

    # Add sub-components to the top-level component
    top_component.add_component(sub_component_1)
    top_component.add_component(sub_component_2)

    # Print the bill of materials
    top_component.print_bom()

    next_component = BillOfMaterials("Product Z", 2)

    next_component.add_component(top_component)

    next_component.print_bom()
    # FIXME:
    # Quantities not calculated!