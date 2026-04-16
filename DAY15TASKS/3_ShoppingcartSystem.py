cart = []
for i in range(5):
    item = input("Enter item name: ")
    try:
        price = float(input("Enter price: "))
        cart.append((item, price))
    except:
        print("Invalid price! Skipping item.")
unique_cart = list(set(cart))
total = 0
for item, price in unique_cart:
    if price > 0:   
        total += price
print("Cart Items:", unique_cart)
print("Total Cost:", total)
