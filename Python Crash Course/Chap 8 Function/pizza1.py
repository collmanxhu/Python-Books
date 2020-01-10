def make_pizza(size, *toppings):          # *toppings : tell python to make an empty tuple
    """summarize the pizza we are going to make"""
    print(f"\nMaking a {size} inch of pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")