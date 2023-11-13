koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

import random
random.shuffle(koloda)

print('BLACKJACK')
count = 0
while True:
    choice = input('whill you take card ? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print('you card %d' %current)
        count += current
        if count > 21:
            print('game over')
            break
        elif count == 21:
            print('happy, you have 21')
            break
        else:
            print('you have %d point.' %count)
    elif choice == 'n':
        print('you have %d point and game over' %count)
        break
