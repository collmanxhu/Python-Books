#4-3 counting to 20
for value in range(1,21):
    print(value)

#4-4 counting to 1 million
values = [value for value in range(1,1000001)]
#print(values)

#4-5 summing 1 million
print(min(values))
print(max(values))
print(sum(values))

#4-6 Odd numbers
values = [value for value in range(1 ,20, 2)]
print(values)

#4-7 multiples of 3
values = [value *3 for value in range(3,31)]
print(values)

#4-8 make list of cubes
values = [value**3 for value in range(1,11)]
print(values)
for value in values:
    print(value)