products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}
categories = {"Stationery"}
cart = []
def calculate_total(cart_items):
    if len(cart_items) == 0:
        return 0
    product, qty = cart_items[0]
    return (products[product] * qty) + calculate_total(cart_items[1:])
def display_products():
    print("\nAvailable Products:")
    for p, price in products.items():
        print(f"{p}: {price}")
def add_to_cart():
    try:
        name = input("Enter product name: ")
        
        if name not in products:
            raise NameError
        
        qty = int(input("Enter quantity: "))
        
        cart.append((name, qty))
        print("Item added to cart successfully.")
    
    except ValueError:
        print("Invalid quantity! Please enter a number.")
    except NameError:
        print("Product not found in store.")
def view_bill():
    try:
        if not isinstance(cart, list):
            raise TypeError
        
        print("\nItems in Cart:")
        for item in cart:
            print(f"{item[0]} x {item[1]}")
        
        total = calculate_total(cart)
        
        if len(cart) == 0:
            raise ZeroDivisionError
        
        print("\nTotal Bill:", total)
    
    except TypeError:
        print("Cart data type error.")
    except ZeroDivisionError:
        print("Calculation error: division by zero.")
while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        display_products()
    elif choice == '2':
        add_to_cart()
    elif choice == '3':
        view_bill()
    elif choice == '4':
        break
    else:
        print("Invalid choice")
