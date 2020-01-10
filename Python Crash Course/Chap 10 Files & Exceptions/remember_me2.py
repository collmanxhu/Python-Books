import json

# 10-11 Favorite numbers. write program to prompt user's input, and read these number
def favorite_number():
    """show user's favorite numbers"""
    filename = 'Python-Proj/user_favorite_num.json'
    try:
        with open(filename) as f:
            user_num = json.load(f)
    except FileNotFoundError:
        user_num = input("Please input your favorite number: ")
        with open(filename, 'w') as f:
            json.dump(user_num, f)
            print(f"Thank you for your input, We'll remember it!")
    else:
        print(f"Your favorite number is: {user_num}.")

favorite_number()

# 10-13 verify user. if not exit, add a new one
def get_stored_username():
    filename = 'Python-Proj/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(input_name):
    """Prompt for a new username"""
    filename = 'Python-Proj/username.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(input_name, f)
    return input_name

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    input_name = input("Whats your name?")
    if username == input_name:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(input_name)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
