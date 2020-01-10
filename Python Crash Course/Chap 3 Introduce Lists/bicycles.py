bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])   # print ist item in the list
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# 3-1 & 3-2 change to print individual item in the list
names = ['angela', 'john', 'peter', 'william', 'bobby']
for name in names:
    print(f"I would like to say 'hi' to {name}")
