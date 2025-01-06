import copy
from products import products
# Original list of products


# 1. Increase prices by 10% and generate new_products by deep copy
new_products = copy.deepcopy(products)
for product in new_products:
    product['Price'] *= 1.10

print('New products with 10% price increase (deepcopy):')
for product in new_products:
    print(f"{product['Product']}: ${product['Price']:.2f}")

print('\n')

# 2. Sort products by name in descending order (Z-A)
sorted_name = sorted(new_products, key=lambda x: x['Product'], reverse=True)

# 3. Generate a deep copy of the products sorted by name
sorted_name_deepcopy = copy.deepcopy(sorted_name)

print('Products sorted by name (descending)(deepcopy):')
for product in sorted_name_deepcopy:
    print(f"{product['Product']}: ${product['Price']:.2f}")

print('\n')

# 4. Sort products by price in ascending order (lowest to highest)
sorted_price = sorted(new_products, key=lambda x: x['Price'])

# 5. Generate a deep copy of the products sorted by price
sorted_price_deepcopy = copy.deepcopy(sorted_price)

print('Products sorted by price (ascending)(deepcopy):')
for product in sorted_price_deepcopy:
    print(f"{product['Product']}: ${product['Price']:.2f}")

print('\n')