# Tic-tac-toe-with-basic AI
Function based verion 

The object of Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. Players alternate placing Xs and Os on the game board until either oppent has three in a row or all nine squares are filled. X always goes first, and in the event that no one has three in a row, the stalemate is called a cat game.

to write  this code i used list as a board to keep a track of user and computer moves,
code have a check-function which contains all 8 possible combinations to win and by each move program checks the positions and if any of combinations happens on the board check-win function returns True and game will stop. 
and i used counter to count the moves so i dont have to write a function for draw positions! it means by end of the 9 moves if 
no winner comes out of the game then game would be draw by default.
normally in this code we use whileloop but i wanted to try using separated fucnctions to call eachother, and because this game wont last long then fuction calls wont raise maximum function dept error.
and a bout implementing some kind a "AI" with my very limited knowledge on the subject, i cameup with the idea that, if we can write a check win fucntion which can check for win combinations, then i can write a fucntion which can check pre win combinations to some depts and perform certain actions. for example as a first move i wrote simple condition that checks if the center is free then it should capture it, if not menas that option is not available anymore and computer need to check the corners, so by this logic i tried to create a tree of choices. and in some points in the game that any move cant change the outcome of the game, i let the computer use random moves to mark available spot.
one mistake that i think i had in my code was using global variables, which i have to avoid using it.

i wrote a gui for this code, the logic of the game is the same but i added some graphics for it.

