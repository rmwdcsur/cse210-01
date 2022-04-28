# CSE 210 - Week 2 - TIC TAC TOE
# Author: Santiago Risso

#Welcome MESSAGE
print("Welcome to TIC TAC TOE Game !!!")

plays_x = []
plays_o = []

def main():
    found_winner = False
    player_one_turn = True
    user_input = 0
    available_plays = [1,2,3,4,5,6,7,8,9]

    while (found_winner == False):
        display_grid(plays_x, plays_o)
        if player_one_turn:
            user_input = int(input("X's turn to choose a square (1-9): "))
            if available_plays.count(user_input) == 1:
                plays_x.append(user_input)
                plays_x.sort()
                available_plays.remove(user_input)
                player_one_turn = False
            else:
                print("Can't play that number! Try again...")

            #Secret way to exit the game
            if user_input == 99:
                found_winner = True
        else:
            user_input = int(input("O's turn to choose a square (1-9): "))
            if available_plays.count(user_input) == 1:
                plays_o.append(user_input)
                plays_o.sort()
                available_plays.remove(user_input)
                player_one_turn = True
            else:
                print("Can't play that number! Try again...")
        if plays_x.count(1) == 1 and plays_x.count(2) == 1 and plays_x.count(3) == 1 \
        or  plays_x.count(1) == 1 and plays_x.count(4) == 1 and plays_x.count(7) == 1 \
        or  plays_x.count(4) == 1 and plays_x.count(5) == 1 and plays_x.count(6) == 1 \
        or  plays_x.count(2) == 1 and plays_x.count(5) == 1 and plays_x.count(8) == 1 \
        or  plays_x.count(3) == 1 and plays_x.count(6) == 1 and plays_x.count(9) == 1 \
        or  plays_x.count(1) == 1 and plays_x.count(5) == 1 and plays_x.count(9) == 1 \
        or  plays_x.count(7) == 1 and plays_x.count(5) == 1 and plays_x.count(3) == 1 \
        or plays_x.count(7) == 1 and plays_x.count(8) == 1 and plays_x.count(9) == 1:
            found_winner = True
            display_grid(plays_x, plays_o)
            print("Player X is the Winner!!!")
        if plays_o.count(1) == 1 and plays_o.count(2) == 1 and plays_o.count(3) == 1 \
        or  plays_o.count(1) == 1 and plays_o.count(4) == 1 and plays_o.count(7) == 1 \
        or  plays_o.count(4) == 1 and plays_o.count(5) == 1 and plays_o.count(6) == 1 \
        or  plays_o.count(2) == 1 and plays_o.count(5) == 1 and plays_o.count(8) == 1 \
        or  plays_o.count(3) == 1 and plays_o.count(6) == 1 and plays_o.count(9) == 1 \
        or  plays_o.count(1) == 1 and plays_o.count(5) == 1 and plays_o.count(9) == 1 \
        or  plays_o.count(7) == 1 and plays_o.count(5) == 1 and plays_o.count(3) == 1 \
        or plays_o.count(7) == 1 and plays_o.count(8) == 1 and plays_o.count(9) == 1:
            found_winner = True
            display_grid(plays_x, plays_o)
            print("Player O is the Winner!!!")
        





#Display the GRID, this will go in a function that receives an array of numbers
def display_grid(plays_x, plays_o):
    print()
    row_1 = ""
    # Column 1
    if plays_x.count(1) == 1:
        row_1 = "X|"
    elif plays_o.count(1) == 1:
        row_1 = "O|"
    else:
        row_1 = "1|"
    # Column 2
    if plays_x.count(2) == 1:
        row_1 = row_1 + "X|"
    elif plays_o.count(2) == 1:
        row_1 = row_1 + "O|"
    else:
        row_1 = row_1 + "2|"
    # Column 3
    if plays_x.count(3) == 1:
        row_1 = row_1 + "X"
    elif plays_o.count(3) == 1:
        row_1 = row_1 + "O"
    else:
        row_1 = row_1 + "3"
    
    row_2 = ""
    # Column 1
    if plays_x.count(4) == 1:
        row_2 = "X|"
    elif plays_o.count(4) == 1:
        row_2 = "O|"
    else:
        row_2 = "4|"
    # Column 2
    if plays_x.count(5) == 1:
        row_2 = row_2 + "X|"
    elif plays_o.count(5) == 1:
        row_2 = row_2 + "O|"
    else:
        row_2 = row_2 + "5|"
    # Column 3
    if plays_x.count(6) == 1:
        row_2 = row_2 + "X"
    elif plays_o.count(6) == 1:
        row_2 = row_2 + "O"
    else:
        row_2 = row_2 + "6"

    row_3 = ""
    # Column 1
    if plays_x.count(7) == 1:
        row_3 = "X|"
    elif plays_o.count(7) == 1:
        row_3 = "O|"
    else:
        row_3 = "7|"
    # Column 2
    if plays_x.count(8) == 1:
        row_3 = row_3 + "X|"
    elif plays_o.count(8) == 1:
        row_3 = row_3 + "O|"
    else:
        row_3 = row_3 + "8|"
    # Column 3
    if plays_x.count(9) == 1:
        row_3 = row_3 + "X"
    elif plays_o.count(9) == 1:
        row_3 = row_3 + "O"
    else:
        row_3 = row_3 + "9"

    print(row_1)
    print("-+-+-")
    print(row_2)
    print("-+-+-")
    print(row_3)
    print()    


# If this file was executed like this:
# > python tictactoe.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
        main()
