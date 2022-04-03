# Project 21.01.2022
# The lotto game - use of random module

import random as rd

lotto_numbers =  []

for number in range(1,50):
    lotto_numbers.append(int(number))

player_numbers = []  

print('Gra lotto - wybór 6 liczb przez użytkownika')

for number in range(6):
    if number==0:
        print('Wybierz pierwszą liczbę:')
        player_numbers.append(int(input('Podaj liczbę z przedziału [1,49]: ')))
    elif number==1:
        print('Wybierz drugą liczbę:')
        player_numbers.append(int(input('Podaj liczbę z przedziału [1,49]: ')))
    elif number==2:
        print('Wybierz trzecią liczbę:')
        player_numbers.append(int(input('Podaj liczbę z przedziału [1,49]: ')))
    elif number==3:
        print('Wybierz czwartą liczbę:')
        player_numbers.append(int(input('Podaj liczbę z przedziału [1,49]: ')))  
    elif number==4:
        print('Wybierz piątą liczbę:')
        player_numbers.append(int(input('Podaj liczbę z przedziału [1,49]: ')))  
    else:
        print('Wybierz szóstą liczbę:')
        player_numbers.append(int(input('Podaj liczbę z przedziału [1,49]: ')))

print('Wybrane przez Ciebie liczby to:', player_numbers )

drawn_numbers_in_the_game = rd.sample(lotto_numbers,6) 

print('Wylosowane liczby w tej edycji gry lotto to:', drawn_numbers_in_the_game)

hit_numbers_in_the_game = []  

for x in player_numbers:  
    for y in drawn_numbers_in_the_game:
        if x == y:
            hit_numbers_in_the_game.append(x)
            
print('Liczba trafionych liczb w grze:', len(hit_numbers_in_the_game))

if len(hit_numbers_in_the_game)>0: 
    print('Gratulacje! Trafione liczby to:', hit_numbers_in_the_game)
else:
    print('Niestety! Spróbuj ponownie.')

if len(hit_numbers_in_the_game)==6:
    print('Wygrana wynosi 1 000 000 zł!')
elif len(hit_numbers_in_the_game)==5:
    print('Wygrana wynosi kilka tysięcy zł!')
elif len(hit_numbers_in_the_game)==4:
    print('Wygrana wynosi kilkaset zł!')
elif len(hit_numbers_in_the_game)==3:
    print('Wygrana wynosi 24 zł!')
else:
    print('Wygrana wynosi 0 zł :(. Aby wygrać pieniądze traf przynajmniej 3 liczby.')
