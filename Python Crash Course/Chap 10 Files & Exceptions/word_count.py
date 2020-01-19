def count_words(filename):
    """Count the approximate number of words in a text file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exit.")
        pass        # use 'pass' here to fail silently
    else:
        """Count the approximate numbers of words in the file"""
        words = contents.split()
        num_words = len(words)
        print(f"The file '{filename}' has about {num_words} words.")

filenames = ['alice in wonderland.txt', 'siddhartha.txt', 'moddy dick.txt', 'little women.txt']
for filename in filenames:
    count_words(filename)

# 10-6 try to catch ValueError when input wrong
"""Add two numbers provided by user and catch ValueError for text input"""
num1 = input("Please provide first number: ")
num2 = input("Please provide second number: ")
try:
    answer = int(num1) + int(num2)
    print(answer)
except ValueError:
    print("Please enter number instead of text.")

# 10-7 Wrap above code in a while loop for continuing entering number
print("give me two numbers, and I'll add them.")
print("enter 'q' to quit.")
while True:
    num1 = input("Please provide first number: ")
    if num1 == 'q':
        break
    num2 = input("Please provide second number: ")
    if num2 =='q':
        break
    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print("please enter numbers instead of text.")
    else:
        print(answer)

