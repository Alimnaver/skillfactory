                    #        Введение в Python
                    # Итоговое задание 5.6.1 (HW-02)
                    #     Создать игру крестики-нолики
                    # Размер поля предполагается равным 3x3.

number_of_cells = 3  # Переменная с количеством ячеек на доске
board = [1,2,3,4,5,6,7,8,9]   # количество ячеек
def drawing_board():
    """Игровое поле"""
    print('_' * 11)
    for i in range(number_of_cells):
        print((' ' * 3 + '|')*3)
        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|')*3)
def progress_game(move, char):
    """Делаем ход"""
    if (move > 9 or move < 1 or board[move - 1] in ('x', 'o')):
        return False
    board[move - 1] = char
    return True
def check_win():
    """Проверяем победителя"""
    winner = False
    victory = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6))
    for pos in victory:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] ==  board[pos[2]]):
            winner = board[pos[0]]
    return winner
def start_game():
    player = 'x'
    step = 1  # номер шага
    drawing_board()
    while (step < 15) and (check_win() == False):
        move = input(player + ': ' + """Введите номер поля(для выхода из игры нажмите: '0'):""")

        if (move == '0'):
            break
        if(progress_game(int(move), player)):
            print('Хороший ход')

            if (player == 'x'):
                player = "0"
            else:
                player = 'x'
            drawing_board()
        step += 1
    else:
        print('Неверный номер, повторите!')
        if (step == 11):
            print("Ничья!")
        else:
            print(check_win() + ' победил!!!')

print("""Игра: 'Крестики-нолики' """)
start_game()













































