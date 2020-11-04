#Mickey "is finding that he doesn't have much patience for games" Saine
#SDEV 220
# This program is designed to simulate a tic-tack-toe game within a 3x3 grid where each player places virtual tokens
#18 October 2020

import time																																#import time for my witty intro
import datetime																															#import date-time because that whole Linux mathematical stuff was silly and I like this one better

def intro():																															#Create my first function to provide my typical witty introductions. 
    print (f'''\t \t \t Welcome to Mickey's Tic-Tack-Toe''')
    print (f''' \t \t ---------------------------------------------------''')			
    print('''\t \t\t\t Version 1.0''') 
    today =datetime.datetime.today()	
    date_Written = datetime.date (2020, 10, 18)																							#Provides the time because I learned about it in a video today, and REALLY liked it, so I included it in my witty intro
    print (f'''\t\t\tPatent Pending,{date_Written: %B %d, %Y}''')																		#Changed the Patent Pending to Reflect this newly learned concept of time
    time.sleep(1)
    print (f''' \t \t ---------------------------------------------------''')	  
    print(f'''You are accessing this program at {today:%H:%M, on %A, %B %d, %Y}''')														#Really just enjoying the time, and want to capture this for later programs
    time.sleep(1)
    print (''' ''')
    print(f'''This program gives two players a chance to go head to head in TIC-TAC-TOE TO THE DEATH!!''')
    print (''' ''')
    time.sleep(1)


def draw_board(p1, p2):																													#Function to draw the full Multidimensional list that I've made that will store statements to play the game
    print('''---------------''')
    for row in range(len(p1)):																											#For Statement to print blank Spaces for unused ones, "X"s for Player 1, and "O's" for Player 2
        for col in range(len(p1[0])):
            if p1[row][col] == 1:
                print("| X", end=' |')
            elif p2[row][col] == 1:
                print("| O", end=' |')
            else:
                print("   ", end='  ')
        print("\n---------------")


def is_won(p):
    for row in p:																														#if statement to check if the rows meet the criteria for a tic-tac-toe
        if row[0] == 1 and row[1] == 1 and row[2] == 1:																					#Basically an "and" statment to make sure the three criteria are met
            return True


    p_transpose = [[row[i] for row in p] for i in range(len(p[0]))]																		#if statement to check if the columns meet the criteria for a tic-tac-toe
    for row in p_transpose:
        if row[0] == 1 and row[1] == 1 and row[2] == 1:
            return True

    if (p[0][0] == 1 and p[1][1] == 1 and p[2][2] == 1) or (p[0][2] == 1 and p[1][1] == 1 and p[2][0] == 1): 							#if statement to check if the columns meet the criteria for a tic-tac-toe
        return True

    return False


def is_correct_move(p1, p2, x, y):																										#Function to ensure that the move is "legitimate" so the game doesn't break or append into a place that doesn't make sense
    if p1[x][y] == 0 and p2[x][y] == 0 and 0 <= x <= 2 and 0 <= y <= 2:																	#If Statement that basically asks if the move will add to the multi-dimensional List between 0 and 2
        return True	
    else:
        return False																													#Or else, return the move is wrong and invoke alternative statement


def is_a_draw(board):																													#Function to determine whether it's a draw, that tests is there are any open places
    for row in board:
        for col in row:
            if col == 0:
                return False
    return True																															#Return Statement to avert this from happening


def game():
    playAgain = 'y'																														#set play again variable to 'y' for the end

    while playAgain.lower() == 'y':  
        p1 = [[0, 0, 0],  																												#clears/prepares the multi-dimensional list for the X player  
              [0, 0, 0],
              [0, 0, 0]]
        p2 = [[0, 0, 0],  																												#clears/prepares the multi-dimensional list for the O player  															
              [0, 0, 0],
              [0, 0, 0]]

        board = [[0, 0, 0],  																											#clears/prepares the multi-dimensional list for the game board 			
                 [0, 0, 0],
                 [0, 0, 0]]
        draw_board(p1, p2)																												#invokes the draw function to draw the board
        turn = 'x'
        while not is_won(p1) and not is_won(p2) and not is_a_draw(board):																#While Statement to continue the game as long as it is already won or a draw
            if turn == 'x':																												#Nested IF statement to determine which player is up. If X, then start X's turn
                x = int(input('''Enter a row (0, 1, or 2) for player X: '''))															#nested row input statement for "X"
                y = int(input('''Enter a column (0, 1, or 2) for player X: '''))														#nested col input statement for "X"

                while not is_correct_move(p1, p2, x, y):																				#while statement Statement for incorrect input statement
                    print('''Please enter a valid row and column values''')																#Statement for incorrect move
                    x = int(input('''Enter a row (0, 1, or 2) for player X: '''))														#Restatement of row input for "X"
                    y = int(input('''Enter a column (0, 1, or 2) for player X: '''))													#Restatement of col input for "X"
                p1[x][y] = 1																											#Statement for Multi-dimensional list for the Player 1
                board[x][y] = 1																											#Statement for Multi-dimensional list for the board
                draw_board(p1, p2)																										#Statement to invoke function re-draw the board with the new move attached
				
                if is_won(p1):																											#If Statement if the Board is won for Player 1 after appending the multi-dimensional statement
                    print('''Player X is won \n FINISH HIM!''')																			#Print Statement for Win that almost makes me want to get better at Tkinter so the speakers scream "finish him"
                    break																												#Program break statement to end the loop if the game is won (so we can go to play again)
                turn = 'o'																												#OR the turn reverts back to Player 2

            elif turn == 'o':																											#Nested IF statement to determine which player is up. If X, then start X's turn																											#else, if the turn is not x, Then the statement continues to start O's turn
                x = int(input('''Enter a row (0, 1, or 2) for player O: '''))															#nested row input statement for "X'
                y = int(input('''Enter a column (0, 1, or 2) for player O: '''))														#nested row input statement for "O"

                while not is_correct_move(p1, p2, x, y):																				#while statement Statement for incorrect input statements
                    print('''Please enter a valid row and column values''')
                    x = int(input('''Enter a row (0, 1, or 2) for player X: '''))														#Restatement of row input for "O"
                    y = int(input('''Enter a column (0, 1, or 2) for player X: '''))													#Restatement of row input for "O"
                p2[x][y] = 1																											#Statement for Multi-dimensional list for the board																										#Statement for Multi-dimensional list for the Player 2
                board[x][y] = 1																											#Statement to re-draw the board with the new move attached
                draw_board(p1, p2)																										#Statement to invoke function re-draw the board with the new move attached
				
                if is_won(p2):																											#If Statement if the Board is won for Player 1 after appending the multi-dimensional statement
                    print('''Player O is won''')																						#Print Statement for Win that almost makes me want to get better at Tkinter so the speakers scream "finish him"
                    break																												#Program break statement to end the loop if the game is won (so we can go to play again)
                turn = 'x'																												#OR the turn reverts back to Player 1

            if is_a_draw(board):																										#If Statement if the redraw determines that the board is filled and it's a draw
                print("It's a Draw! Time for the next round!")																			#Prints statment to let you know that you both did not win!

        playAgain = input('''Do you want to play again? y or n ''')																		#Input Statement to encourage the loop to start again
		
def main():																																#Main Function
    intro()																																#Plays Dorky introduction
    game()																																#invoke the game function to play TIC-TAC-Toe!!!
	
main()