import os

s = input('would you like to shutdown? \n y \n n \n ==')

if s == 'n':

    exit()

else:
    os.system('shutdown /s /t 1')