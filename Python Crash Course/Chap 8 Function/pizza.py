# passing an Arbitrary numbers of arguments
def make_pizza(*toppings):          # *toppings : tell python to make an empty tuple
    """Print the list of toppings provided"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):          # *toppings : tell python to make an empty tuple
    """Print the list of toppings provided"""
    print(f"\nThe lists : {toppings}")
    print("\nMaking a pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# mixing positional and arbitrary arguments
def make_pizza(size, *toppings):          # *toppings : tell python to make an empty tuple
    """summarize the pizza we are going to make"""
    print(f"\nMaking a {size} inch of pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(10, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# using arbitrary keyword arguments, accept as many key-value pairs as you want
def build_profile(first, last, **user_info):                   # '**' cause python to produce an empty dictionary
    """build a dictionary containing everything you want"""    # **kwargs are often used to collect non-specific keyword arguments
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein', field='physics')
print(user_profile)
user_profile = build_profile('albert', 'einstein', field='physics', location='princeton')
print(user_profile)

# 8-13 Sandwiches : accept a list of items to make sandwich, one arbitrary argument is needed.
def make_sandwich(sandwich_type, *recipes):
    """summarize the sandwich we are going to make"""
    print(f"\nMaking a {sandwich_type} sandwich with following recipe:")
    for recipe in recipes:
        print(f"- {recipe}")
make_sandwich('chicken', '1/2 cup chicken shredded', 'olive oil', 'salt')

# 8-13 build car info using dictionary, must have manufacturer and model name
def make_car(maker, model, **model_info):
    model_info['maker'] = maker
    model_info['model'] = model
    return model_info
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)