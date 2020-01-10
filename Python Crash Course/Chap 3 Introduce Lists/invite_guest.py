#Exercise 3-4, Guest list to be invited
guests = ['peter', 'john', 'joice', 'angela', 'albert']
message = f"\nHello {guests[0].title()}, I would like to invite you to my dinner."
print(message)
print(f"\nHello {guests[1].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[2].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[3].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[4].title()}, I would like to invite you to my dinner.")

#Exercise 3-5, one of the guest cannot attend the dinner. Replace him with another guest.
guests = ['john', 'marry', 'elsa', 'david', 'joyce', 'william']
print(f'It is unhappy that {guests[2].title()} cannot join my dinner')
guests[2] = 'elen'
print(guests)
print(f"\nHello {guests[0].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[1].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[2].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[3].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[4].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[5].title()}, I would like to invite you to my dinner.")

#Exercise 3-6, bigger table is found, more guests are OK, add 3 more guests
print(f"\nHello {guests[0].title()}, a bigger table is found and more guests can be entertained.")
print(f"\nHello {guests[1].title()}, a bigger table is found and more guests can be entertained.")
print(f"\nHello {guests[2].title()}, a bigger table is found and more guests can be entertained.")
print(f"\nHello {guests[3].title()}, a bigger table is found and more guests can be entertained.")
print(f"\nHello {guests[4].title()}, a bigger table is found and more guests can be entertained.")
print(f"\nHello {guests[5].title()}, a bigger table is found and more guests can be entertained.")
guests.insert(0, 'bobby')
guests.insert(3, 'louis')
guests.append('collin')
print('\n')
print(guests)
print(f"\nHello {guests[0].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[1].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[2].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[3].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[4].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[5].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[6].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[7].title()}, I would like to invite you to my dinner.")
print(f"\nHello {guests[8].title()}, I would like to invite you to my dinner.")

#Exercise 3-7, bigger table is not ready, only 2 guests can be invited.
print('Sorry, big table is not ready, only 2 guests can be invited')
popped_guest = guests.pop()
print(f"\nSorry {popped_guest}, table is full, you are not invited")
popped_guest = guests.pop()
print(f"\nSorry {popped_guest}, table is full, you are not invited")
popped_guest = guests.pop()
print(f"\nSorry {popped_guest}, table is full, you are not invited")
popped_guest = guests.pop()
print(f"\nSorry {popped_guest}, table is full, you are not invited")
popped_guest = guests.pop()
print(f"\nSorry {popped_guest}, table is full, you are not invited")
popped_guest = guests.pop()
print(f"\nSorry {popped_guest}, table is full, you are not invited")
popped_guest = guests.pop()
print(f"\nSorry {popped_guest}, table is full, you are not invited")
print("\n")
print(guests)
del guests[0]
del guests[0]
print(guests)
#
