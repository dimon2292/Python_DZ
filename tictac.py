EMPTY = ''
X = 'X'
о = '0'
NUM_SQUARES = 9
TIE = 'Ничья'


def display_instruct():                                     # отображает поле с номерами ячеек
    print('Добро пожаловать в игру крестики-нолики!')
    print('ваша задачи - выставить в ряд 3 крестика или 3 нолика по горизонтали, вертикали или диагонали')
    print('номера полей - как указано ниже:')
    board = [i for i in range(NUM_SQUARES)]
    print('\n\t', board[0], ' | ', board[1], ' | ',board[2])
    print('\t', board[3], ' | ', board[4], ' |',board[5])
    print('\t', board[6], ' | ', board[7], ' | ',board[8], '\n')
    print('УДАЧНОЙ ИГРЫ!')


def new_board(NUM_SQUARES) -> list:                                     #создаёт игровую доску
    board = [EMPTY for i in range(NUM_SQUARES)]
    return board


def ask_yes_no(question) -> str:                                       #пользовательский ввод Да или Нет
    response = None
    while response not in('yes', 'no'):
        response = input(question).lower()
    return response


def ask_number(question, low, high) -> int:                #пользовательский ввод Поля куда будет ходить
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():                                                    #Кто первый ходит
    go_first = ask_yes_no('вы ходите первым(крестиками)? Введите yes или no')
    if go_first == 'yes':
        player_1 = X
        player_2 = о
    else:
        player_1 = о
        player_2 = X
    return player_1, player_2


def display_board(board):                                           #Отрисовывает доску
    print('\n\t', board[0], ' | ', board[1], ' | ', board[2])
    print('\t', board[3], ' | ', board[4], ' |', board[5])
    print('\t', board[6], ' | ', board[7], ' | ', board[8], '\n')


def legal_moves(board) -> list:                                     #Список возможных ходов
    moves = [i for i in range(NUM_SQUARES) if board[i] == EMPTY]
    return moves


def winner(board):                                          #Условия победы, ничьи, продолжения хода
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for i in  WAYS_TO_WIN:
        if board[i[0]] == board[i[1]] == board[i[2]] != EMPTY:
            winner = board[i[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None


def player_move(board):                      #ход игрока
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('введите цифру от 0 до 8', 0, NUM_SQUARES)
    return move


def next_turn(turn):                                    #тип фишек
    if turn == X:
        return о
    else:
        return X


def congrat_winner(the_winner, player_1, player_2):                 #сообщения при завершении игры
    if the_winner == player_1:
        print(f'победил игрок {player_1}')
    elif the_winner == player_2:
        print(f'победил игрок {player_2}')
    elif the_winner == TIE:
        print('ничья')


def main():
    display_instruct()
    player_1, player_2 = pieces()
    turn = X
    board = new_board(NUM_SQUARES)
    display_board(board)
    while not winner(board):
        if turn == player_1:
            move = player_move(board)
            board[move] = player_1
        else:
            move = player_move(board)
            board[move] = player_2
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, player_1, player_2)


main()
input('нажмите Enter чтобы выйти')