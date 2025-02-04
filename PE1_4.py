#the price of an item after a 25% reduction
price = 99.99
discountPercent = 25
markdown = discountPercent / 100 * price
price -= markdown
print(f"Price = {price:.2f}")