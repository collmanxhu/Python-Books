# Using input() function
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# clen input statement
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is you first name? "
name = input(prompt)
print(f"\nHello {name}!")

# modulo operator : %
remainder = 7 % 2
print(remainder)

# check for even number
number = input("Please enter a number. I'll tell its even or odd. ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
    
