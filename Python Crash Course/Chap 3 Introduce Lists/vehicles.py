motorcycles = ['honda','yamaha', 'suzuki']
print(motorcycles)
print(motorcycles[0])
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(0, 'rollroyces')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)