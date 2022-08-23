# Update - 23/08/2022
# The lotto game 

import numpy as np

LOTTO_NUMBERS =  np.array(np.arange(1,50))

def user_choice() -> list[int]:
    index = 1
    player_numbers = []  

    while index < 7:
        print(f'Wybierz liczbę nr {index}:')
        choice = int(input('Podaj liczbę z przedziału [1,49]: '))

        if choice in player_numbers:
            print('Podane liczby muszą być unikalne.')
        elif choice in range(1,50):
            player_numbers.append(choice)
            index += 1
        else:
            print('Podana liczba musi być z przedziału [1,49].')

    return np.array(player_numbers)


def print_raport(hit_numbers_in_the_game:list[int]) -> None:
            
    print('Liczba trafionych liczb w grze:', len(hit_numbers_in_the_game))

    if len(hit_numbers_in_the_game)>0: 
        print('Gratulacje! Trafione liczby to: ', hit_numbers_in_the_game)

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

    else:
        print('Niestety! Spróbuj ponownie.')
        print('Wygrana wynosi 0 zł :(. Aby wygrać pieniądze traf przynajmniej 3 liczby.')


def main():
    print('Gra lotto - wybór 6 liczb przez użytkownika')

    user_numbers = user_choice()
    print('Wybrane przez Ciebie liczby to:', user_numbers)

    drawn_numbers_in_the_game = np.random.choice(LOTTO_NUMBERS,6) 
    print('Wylosowane liczby w tej edycji gry lotto to: ', drawn_numbers_in_the_game)
    
    hit_numbers_in_the_game = [x for x in user_numbers for y in drawn_numbers_in_the_game if x==y] 

    print_raport(hit_numbers_in_the_game)


if __name__ == '__main__':
    main()
