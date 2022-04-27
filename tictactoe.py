# CSE 210 - Week 2 - TIC TAC TOE
# Author: Santiago Risso

#Welcome MESSAGE
print("Welcome to TIC TAC TOE Game !!!")

def main():
    found_winner = False
    player_one_turn = True
    user_input = 0
    while (found_winner == False):
        display_grid()
        if player_one_turn:
            user_input = input("X's turn to choose a square (1-9): ")
            player_one_turn = False
        else:
            user_input = input("O's turn to choose a square (1-9): ")
            player_one_turn = True
        





#Display the GRID, this will go in a function that receives an array of numbers
def display_grid():
    print()
    print("1|2|3")
    print("-+-+-")
    print("4|5|6")
    print("-+-+-")
    print("7|8|9")
    print()


# If this file was executed like this:
# > python tictactoe.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
        main()
