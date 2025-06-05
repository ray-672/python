theboard = {'7':' ','8':' ','9':' ',
            '4':' ','5':' ','6':' ',
            '1':' ','2':' ','3':' ',}

boardkeys = []

for key in theboard:
    boardkeys.append(key)


def printboard(board):
    print(board['7']+ '|'+ board['8'] + '|' + board['9'])
    print('+-+-+')
    print(board['4']+ '|'+ board['5'] + '|' + board['6'])
    print('+-+-+')
    print(board['1']+ '|'+ board['2'] + '|' + board['3'])
    print('+-+-+')

def game():
        turn = 'x'
        count = 0

        for i in range(10):
            printboard(theboard)
            print(count)

            print('its your turn'+turn+' \nwhat is your move?')

            move = input()

            if theboard[move] == ' ':
                theboard[move] = turn
                count=+1

            else:
                print('the place is already filled')
                continue

            if count <=5:
                if theboard['7'] == theboard['8'] == theboard['9'] !=' ':
                    printboard(theboard)
                    print('\ngame over\n')
                    print(turn+'won')
                    break

                elif theboard['4'] == theboard['5'] == theboard['6'] !=' ':
                    printboard(theboard)
                    print('\ngame over\n')
                    print(turn+'won')
                    break

                elif theboard['1'] == theboard['2'] == theboard['3'] !=' ':
                    printboard(theboard)
                    print('\ngame over\n')
                    print(turn+'won')
                    break

                

                

                elif theboard['2'] == theboard['5'] == theboard['8'] !=' ':
                    printboard(theboard)
                    print('\ngame over\n')
                    print(turn+'won')
                    break

                elif theboard['3'] == theboard['6'] == theboard['9'] !=' ':
                    printboard(theboard)
                    print('\ngame over\n')
                    print(turn+'won')
                    break

                elif theboard['7'] == theboard['5'] == theboard['3'] !=' ':
                    printboard(theboard)
                    print('\ngame over\n')
                    print(turn+'won')
                    break

                elif theboard['1'] == theboard['5'] == theboard['9'] !=' ':
                    printboard(theboard)
                    print('\ngame over\n')
                    print(turn+'won')
                    break
            if count == 9:
                print('game over it is a tie')
            
            if turn  == 'x':
                turn = 'o'

            else:
                turn = 'x'

        restart = input('do you want to play again (y/n)')
        if restart == 'y' or restart == 'Y':
            for key in boardkeys:
                theboard[key] = ' '


        game()

if __name__ == '__main__':
    game()
    