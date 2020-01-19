motorcycles = ['honda', 'yamaha', 'suzuki', 'docuti']
motorcycles.append('toyota')
last_owned = motorcycles.pop()
print(f"The last motorcycles I owned was a {last_owned.title()}.")   #To create an f-string, prefix the string with the letter “ f ”. The string itself can be formatted in much the same way that you would with str.format(). F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.]
first_owned = motorcycles.pop(0)
print(f"The first motorcycles I owned was a {first_owned.title()}.")
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'docuti']
too_expensive = 'docuti'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive too me.")
motorcycles.insert(0, 'ducati')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
