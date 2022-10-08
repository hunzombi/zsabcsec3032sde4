import sys
import random

game = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def check_winner(x):
    for row in game:
        if row.count(x) == 3:
            return True
    if game[0][0] == x and game[1][0] == x and game[2][0] == x:
        return True
    if game[0][1] == x and game[1][1] == x and game[2][1] == x:
        return True
    if game[2][2] == x and game[1][2] == x and game[2][2] == x:
        return True
    if game[0][0] == x and game[1][1] == x and game[2][2] == x:
        return True
    if game[0][2] == x and game[1][1] == x and game[2][0] == x:
        return True
    return False

def check_full():
    for row in game:
        if row.count(" ") > 0:
            return False
        return True

def chooserand():
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    if game[row][col] == " ":
        return [row, col]
    else:
        return chooserand()

def print_game():
    for y, row in enumerate(game):
        print("{} | {} | {}\n".format(game[y][0], game[y][1], game[y][2]))


def main():
    player1 = "X"
    player2 = "O"
    won = False
    winner = None

    while not won and not check_full():
        print_game()
        ask = input("choose where do you want to place the X (syntax = '0 0'): ")
        a, b = ask.split()
        a = int(a)
        b = int(b)
        if game[a][b] != " ":
            print("Please input a valid square!")
            continue
        game[a][b] = f"{player1}"
        if check_full():
            break
        if check_winner(player1):
            won = True
            winner = player1
            break
        arr = chooserand()
        c, d = arr[0], arr[1]
        game[c][d] = player2
        if check_full():
            break
        if check_winner(player2):
            won = True
            winner = player2
    
    print_game()
    if won:
        print(f"\n\nThe {winner} player won!")
    else:
        print("It's a Draw!")


if __name__ == '__main__':
    main()