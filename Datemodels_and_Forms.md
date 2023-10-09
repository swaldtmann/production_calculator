# Description or brainstorming for data model and Forms

## Data Model

### Product

Products could be produceable or raw materials. If they are produceable, they shall have a recipe, which should recurse to raw materials in the last step.

### Recipe

Recipes contain the intermediate products or raw materials to produce the product. Has a batch size and the amounts of the ingredients.

### BOM - bill of materials

When an amount of products shall be calculated, the BOM holds the amount and type of products or raw materials.

## Forms

### Product Input Screen (PIS)

#### PIS Fields

- Text: Product Name
- Int: Batch Size
- Select: Recipe or Raw Material
  - List of
    - Dropdown: Product
    - Int: Amount

#### PIS Functions

- Add new
- Edit
- Delete
- Export Yaml
- Import Yaml

### Production Calculator (PC)

#### PC Fields

- Dropdown select:  Product
- Int: Amount to calculate

#### PC Functions

- Calculate
- Clear
- Export Yaml
