# total = 0   UnboundLocalError: local variable 'total' referenced before assignment
def multiply(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(multiply(2, 3, 4, 5))


def fizz_buzz(input):
    if input % 3 == 0:
        result = 'Fizz'
    else:
        result = 'Buzz'
    return result
print(fizz_buzz(5))


def fizz_buzz(input):
    if input % 3 == 0:
        return 'Fizz'
    else:
        return 'Buzz'
print(fizz_buzz(5))

numbers = [12, 34, 1, 4, 4, 67, 37, 9, 0, 81]
# Approach 1
result = []
for index in range(len(numbers)):
    if numbers[index] > 5:
        result.append(numbers[index])
print(result)  #Prints [12, 34, 67, 37, 9, 81]

# Approach 2 (Slightly cleaner, for-in loops)
result = []
for number in numbers:
    if number > 5:
        result.append(number)
print(result)  #Prints [12, 34, 67, 37, 9, 81]

# Approach 3 (Enter List Comprehension)
result = [number for number in numbers if number > 5]

# or more generally:
# [function(number) for number in numbers if condition(number)]