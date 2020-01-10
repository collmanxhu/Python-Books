players = ['martina', 'michael', 'florence', 'eli', 'charles']
print(players[0:3])
print(players[1:5])
print(players[:5])
print(players[2:])
print(players[-3:])
for player in players:
    print(player.title())
guests = players
print(guests)
guests = players[:]
print(guests)
guests.append('alice')
print(guests)

#4-10 print message
print('\nThe first three items in the lists are:')
print(players[0:3])
print('\nThree items in the middle of the lists are:')
print(players[1:4])
print('\nThe last three items in lists are:')
print(players[-3:])