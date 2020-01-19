alien_0 = {'color':'green', 'points':5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)

#determine how far to the right the alien should move
alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")
#Move the alien to the right. Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] = x_increment
print(f"New postion: {alien_0['x_position']}")