''' tic tac toe with AI by: Khashayar Nariman ** Xerex ** 5/1/2018
 the idea is to check some possibelities in each state of the game.
 
 in each move computer checks for:
 if game is already in win state or tie state.
 if game is not in win or tie then start checking the tree.
 if made moves are less than 3 then will capture one of corners and center.
 aftre second move starts checking for possible win move.
 if possible win move not available starts checking for blocking move to prvent human from
 winning.
 if blocking wasnt available will goes for random move
 so basically i tried to avoid unnecessary calculations, and copy the main board.
 tie game based on how many move has been played, if check win is false on crtain number
 game should be tie.
 '''
import random, time, os

board = [" "]*9
count = 0

#-- All possible win positions 
win_positions =[[0,1,2],[3,4,5],[6,7,8],
                [0,3,6],[1,4,7],[2,5,8],
                [0,4,8],[2,4,6]]
#-- Board corners, which will be used in first and second move 
corners = [0,2,6,8]

#-- All postential positions to become win positions after one move
semi_positions =[[0,1,2],[0,2,1],[1,2,0],
                 [3,4,5],[3,5,4],[4,5,3],
                 [6,7,8],[6,8,7],[7,8,6],
                 [0,3,6],[0,6,3],[3,6,0],
                 [1,4,7],[1,7,4],[4,7,1],
                 [2,5,8],[2,8,5],[5,8,2],
                 [0,4,8],[0,8,4],[4,8,0],
                 [2,4,6],[2,6,4],[4,6,2]]

#-- Visual the board, with little spice of time 
def show(board):
    os.system("clear")
    time.sleep(0.10)
    print(board[0],"|",board[1],"|",board[2])
    time.sleep(0.10)
    print("----------")
    time.sleep(0.10)
    print(board[3],"|",board[4],"|",board[5])
    time.sleep(0.10)
    print("----------")
    time.sleep(0.10)
    print(board[6],"|",board[7],"|",board[8])
    time.sleep(0.10)
    print("----------")
    time.sleep(0.10)
show(board)

#-- After each move for player and computer will be checked if game is over or not 
def check_win(board):
    global count
    for first, second, third in win_positions:
        if board[first] == board[second] == board[third] and board[first] != " ":
            print(first, second, third)
            return True

#-- Function to get move input from user, and check for win, tie, and return the turn to
#-- to computer
def user(board):
    global count
    if count == 9:
        print("tie")
        main()
    else:
        move = "x"
        spot = int(input(" make a move: "))
        if board[spot] !=" ":
            print("Spot is taken, try another spot!")
            user(board)
        board[spot] = move
        count += 1
        show(board)
        if check_win(board):
            print("You win")
            main()
        elif count == 9:
            if check_win(board) != True:
                print("tie")
                main()
        else:
            computer(board)

#-- i tried to build a node system with next 4 functions

#-- Returning the first and second move, after second move it will call the next function
def get_tree(board):
    global count
    move = "o"
    print("starting a tree....")
    time.sleep(0.10)
    global count
    if count == 0:
        spot = random.choice(corners)
        board[spot] = move
        count += 1
        
        show(board)
        user(board)
    
    elif count == 1:
        if board[4] == " ":
            board[4] = move
            count += 1
            show(board)
            user(board)
        else:
            spot = random.choice(corners)
            board[spot] = move
            count += 1
            show(board)
            user(board)
            
    elif count >= 2:
        get_win(board)

#-- Here it checks for next possible winning move! if not, it will call the next function 
def get_win(board):
    global count
    print("check for a win move....")
    time.sleep(0.10)
    for f,s,t in semi_positions:
        if board[f]== "o" and board[s]=="o":
            print(f,s," are taken")
            if board[t] != "x" and board[t] != "o":
                print("found: ", t)
                board[t] = "o"
                count += 1
                show(board)
                if check_win(board):
                    print("Game over")
                    main()
                else:
                    user(board)
#-- Here it checks for next possible human winning move and blocks it, if not, will call the
#-- the random function 
def get_block(board):
    global count
    print("check for a block move....")
    time.sleep(0.10)
    for f,s,t in semi_positions:
            if board[f]== "x" and board[s]=="x":
                print(f,s," are taken")
                if board[t] != "x" and board[t] != "o":
                    print("found: ",t)
                    board[t] = "o"
                    count += 1
                    show(board)
                    time.sleep(0.10)
                    user(board)

#-- and finally it will calls the random function
#-- here i had a problem when i returned the value to computer function, some times i got
#-- None type Value, and i coudnt fix it, so basically i decided to make a computer move
#-- right inside the function itself 
def get_random(board):
    global count 
    move = "o"
    print("check for random available move")
    time.sleep(0.10)
    spot = random.randrange(0,9)
    if board[spot] != " ":
        get_random(board)
    if board[spot] == " ":
        print("Found random: ", spot)
        time.sleep(0.10)
        board[spot] = move
        count += 1
        show(board)
        user(board)

#-- This is the main computer function,  all the other functions related to computer move
#-- will be called from this function and return the possible move to this one, except
#-- ranodm function which as i said, i had a problem with!
def computer(board):
    global count
    if check_win(board)!= True:
        if count == 9:
            print("Game is tie")
            main()
            
        else:
            move = "o"
            spot = get_tree(board)
            print(spot)
            time.sleep(0.10)
            if spot == None:
                get_block(board)
                if spot == None:
                    get_random(board)

            print( "recieved spot: ", spot)
            time.sleep(0.10)
            board[spot] = move
            count += 1
            show(board)
            user(board)

#-- Makes a random choice for first player   
def who_goes_first():
    play = input("wanna play? y/n ")
    if play == "y".lower():
        first = random.randrange(0,2)
        if first == 0:
            print("your turn")
            time.sleep(1)
            show(board)
            user(board)
        else:
            print("my turn")
            time.sleep(1)
            computer(board)
    if play == "n".lower():
        time.sleep(1)
        print(" bye bye")
        exit()
#-- and the main function is for reseting the count, and the board 
def main():
    print("************************")
    print("Wellcome to Tic, tc, toe")
    print("************************")
    global count, board
    reset_board = [" "]*9
    reset_count = 0 
    board = reset_board
    count = reset_count
    who_goes_first()
    
if __name__ == "__main__":
    main()
