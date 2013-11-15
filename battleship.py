from random import randint

board = []

# Create a 5x5 board by making a list of 5 "0" and repeat it 5 times:
for element in range(5):
    board.append(["O"] * 5)

# To print each outer list of a big list. 1 outer list = 1 row:
def print_board(board):
    for row in board:
        print " ".join(row) # to concatenate all the elements inside the list into one string => to make the board look pretty

print "Let's play Battleship!"
print_board(board) # display the board

# Assign a random location (random row & column) for my ship. This location will be hidden:
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row
#print ship_col

# User can play 4 turns before game over (turn starts from 0 to 3):
for turn in range(4):
    # Ask user to guess my ship's location:
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Column: "))

    # A winning case:
    if guess_row == ship_row and guess_col == ship_col: # raw_input will return a string => have to make (guess_row & guess_col) become integer to compare with number
        print "Congratulations! You sunk my battleship!"
        break # to get out of a loop and stop a game if user wins
    # Wrong cases:
    else: 
        # If user's guess is invalid or off the board:
        if guess_row > len(board)-1 or guess_col > len(board[0])-1: 
            print "Oops, that's not even in the ocean."
        # If user already guessed a specific location:
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
        # If user guess it wrong:
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X" # mark X on a location that is already guessed 
        # Notify user when they play all 4 turns:
        if turn == 3:
            print "GAME OVER!!! Too bad you just lost your last chance :(. Try again :)"
            break # to end a game without displaying turn and a board
    
    # Display user's turn:
    if turn == 0:
        print "You've played ", turn + 1, "turn"
    else:
        print "You've played ", turn + 1, "turns"
    # Display the board again:
    print_board(board)