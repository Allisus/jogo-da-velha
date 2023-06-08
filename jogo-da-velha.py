def print_board(board):
    for row in board:
        print("I".join(row))
        print("-----")

def check_winner(board):
    # Verificar linhas
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Verificar colunas
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Verifica diagonais
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    concurrent_player = "X"

    while True:
        print_board(board)

        row = int(input("Escolha a linha (0-2)"))
        col = int(input("Escolha a coluna (0-2)"))

        if board[row][col] == " ":
            board[row][col] = concurrent_player
        else:
            print("Essa posição já esta ocupada, Tente novamente.")
            continue

        if check_winner(board):
            print_board(board)
            print(f"O jogador {concurrent_player} venceu!")

        if " " not in [cell for row in board for cell in row]:
            print_board(board)
            print("Empate!")
            break

        concurrent_player = "O" if concurrent_player == "X" else "X"

play_game()