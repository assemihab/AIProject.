from board import Board
import time
import random
import gui,AI_algorithms
import numpy as np

# GAME LINK
# http://kevinshannon.com/connect4/

def main():
    alg_selected,diff_level=gui.s_d_gui()
    agent= 1
    computer= 0
    turn=1
    board = Board()
    time.sleep(3)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        # board.print_grid(game_board)

        # YOUR CODE GOES HERE
        if turn == computer:
            time.sleep(2)
            turn+=1
            turn=turn%2


	# Ask for Player 2 Input
        if turn == agent:				
            board.print_grid(game_board)
            randomcolIndex=6
            if alg_selected==1:
                    
                array=np.array(game_board)
                print('this is the game board for testing',game_board )
                
                Val,boardd,col=AI_algorithms.MinimaxAlgorithm(array,diff_level,agent,randomcolIndex)
                print('the column you have selected is', col)
                if(col==10000):
                        col=6
                board.select_column(col)
            else:
                array=np.array(game_board)
                print('this is the game board for testing',game_board )
                Val,boardd,col=AI_algorithms.alphaBetaPruning(array,diff_level,agent,randomcolIndex)
                print('the column you have selected is', col)
                if(col==10000):
                    col=6
                board.select_column(col)
            turn += 1
            turn = turn % 2

        time.sleep(2)


if __name__ == "__main__":
    main()
