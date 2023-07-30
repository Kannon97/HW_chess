# Создание пустого поля 3x3
board = [["-" for _ in range(3)] for _ in range(3)]


# Функция для печати поля в консоль
def print_board(board):
    print("  0 1 2")
    for i in range(3):
        row = " ".join(board[i])
        print(f"{i} {row}")


# Функция для проверки победы
def check_win(board, symbol):
    # Проверка горизонтальных линий
    for row in board:
        if row.count(symbol) == 3:
            return True

    # Проверка вертикальных линий
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] == symbol or board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False


# Игровой цикл
current_player = "x"

while True:
    print_board(board)
    print(f"Ход игрока '{current_player}'")

    # Обработка ввода игрока
    while True:
        try:
            row = int(input("Введите номер строки (0-2): "))
            col = int(input("Введите номер столбца (0-2): "))
            if not (0 <= row <= 2 and 0 <= col <= 2):
                raise ValueError
            if board[row][col] != "-":
                raise ValueError
            break
        except ValueError:
            print("Ошибка ввода. Попробуйте еще раз.")

    # Размещение символа на поле
    board[row][col] = current_player

    # Проверка победы
    if check_win(board, current_player):
        print_board(board)
        print(f"Игрок '{current_player}' победил!")
        break
    # Проверка ничьей
    elif all(board[i][j] != "-" for i in range(3) for j in range(3)):
        print_board(board)
        print("Ничья!")
        break

    # Смена игрока
    current_player = "o" if current_player == "x" else "x"