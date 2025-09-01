#!/usr/bin/python3

def print_board(board):
    """
    Affiche le plateau de jeu sous forme de grille 3x3.
    Chaque case est séparée par des barres verticales et des tirets.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board):
    """
    Vérifie si un joueur a gagné.
    Retourne le symbole du gagnant ('X' ou 'O') si victoire, sinon None.
    """
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Diagonale principale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    # Diagonale secondaire
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    """
    Vérifie si le plateau est rempli (match nul).
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Fonction principale du jeu :
    - Initialise le plateau
    - Alterne les tours entre les joueurs X et O
    - Gère les entrées utilisateur et les erreurs
    - Affiche le gagnant ou un match nul
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position. Please choose between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Changement de joueur
        player = "O" if player == "X" else "X"

# Lancement du jeu
tic_tac_toe()