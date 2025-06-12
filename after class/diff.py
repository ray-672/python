setx = {'pink','blue'}
sety = {'red','pink'}
print('the original sets')
print(setx)
print(sety)

print('\nintersets of the two:')
setz = setx.intersection(sety)
print(setz)

sys = setx.symmetric_difference(sety)

