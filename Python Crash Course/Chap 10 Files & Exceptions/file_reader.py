with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("your birthday appears in the first million digits of pi!")
else:
    print("your birthday does not appear in the first million digits of pi.")

with open('learn_python.txt') as file_object:
    for line in file_object:
        print(f"first {line.rstrip()}")
    alines = file_object.readlines()
    for aline in alines:
        print(aline)

filename = 'Python Crash Course/programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I dfsdffsljkkjfdklfjsf;jl.\n")
    file_object.write("erotinxfsklndffdklflkdfldfj.\n")