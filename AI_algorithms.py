#!/usr/bin/env python
# coding: utf-8

# In[143]:

#### initial state######
###### noteeeeee######
##### 1 is the AGENT
##### 2 is the Computerrrrrrrrrr
import tkinter as tk
import numpy as np

agent= 1
computer= 2
'''
row = []
board = []

for i in range(colSize):
    row.append(0)
for i in range(rowSize):
    board.append(row)

board=np.array(board)

board

'''

# In[144]:

colSize=7
rowSize=6
##the board will be 2d list the 
#the column should be the column number
# #the player will be Agent or Computer and used to determine the piece color

def get_col(board, col):
    coll=[]
    board = board.copy()
    for row in range(5,-1,-1):
        if board[row][col] == 0:
            coll = board[row][col]
    
    return coll

def is_validMove(Board,Column):
    Column=Column-1
    #index =get_col(Board,Column) 
    #index = np.where(Board[:, Column] == 0)[0]
    index = [i for i in range(len(Board)) if Board[i][Column] == 0]
    if(len(index)==0):
        return False
    else:
        return True


def dropPiece(Board,column,Player):
    isvalid=is_validMove(Board,column)
    column=column-1
    if(isvalid):
        #index=np.where(Board[:,column]==0)[0]
        index = [i for i in range(len(Board)) if Board[i][column] == 0]
        newboard=Board.copy()
        newboard[index[-1]][column]=Player
        return newboard,column,True
    else:
        return None,None,False


# In[145]:


def getAllValidChildren(Board,Player):
    children=[]
    for i in range (1,colSize+1):
        child,colindex,status=dropPiece(Board,i,Player)
        if(status):
            ##to test the function
            # print(child)
            chillddd={'childd':child,'colindexx':colindex}
            children.append(chillddd)
    return children


# In[146]:

'''
board=np.array([
        [0, 0, 0, 0, 5, 0, 0],
       [0, 0, 0, 0, 5, 0, 0],
       [0, 0, 0, 0, 5, 0, 0],
       [0, 0, 0, 0, 5, 0, 0],
       [0, 0, 0, 0, 5, 0, 0],
       [0, 0, 0, 0, 5, 0, 0]])


# In[147]:


nPP,colindex,status=dropPiece(Board,5,1)
print(nPP)
print(colindex)


# In[148]:


children=getAllValidChildren(Board,1)
print(children)

'''
# In[149]:


def check_goal_test(Board, Player):

    for row in range(6):
        for col in range(4):
            if (
                Board[row][col] == Player and
                Board[row][col+1]== Player and
                Board[row][col+2] == Player and
                Board[row][col+3] == Player
            ):
                return Player

    for col in range(7):
        for row in range(3):
            if (
               Board[row][col] == Player and
                Board[row+1][col]== Player and
                Board[row+2][col] == Player and
                Board[row+3][col] == Player
            ):
                return Player

    for row in range(3):
        for col in range(4):
            if (
                Board[row][col] == Player and
                Board[row+1][col+1]== Player and
                Board[row+2][col+2] == Player and
                Board[row+3][col+3] == Player
            ):
                return Player

    for row in range(3):
        for col in range(3, 7):
            if (
                Board[row][col] == Player and
                Board[row+1][col-1]== Player and
                Board[row+2][col-2]== Player and
                Board[row+3][col-3] == Player
            ):
                return Player
    return False


# In[150]:

# status=check_goal_test(nPP,1)
# print(status)


# In[151]:


def evalLine(line, player, opponent):
    player_count = np.count_nonzero(line==player)
    opponent_count=np.count_nonzero(line==opponent)
    empty_count = np.count_nonzero(line==0)
    if player_count==4 and empty_count==0:
        return 1000
    elif player_count == 3 and empty_count == 1: # If player has 3-in-a-row column/row/diagonal gives heuristic 10
        return 5 
    elif player_count == 2 and empty_count == 2: 
        return 2  
    elif opponent_count == 3 and empty_count == 1:  # If opponent has 3-in-a-row column/row/diagonal gives heuristic -8
        return -4 
    elif opponent_count == 2 and empty_count == 2:
        return -3  
    else:
        return 0


# In[152]:


def UtilityOfBoard(Board, Player, Opponent):
    utility = 0
    
    for row in range(rowSize):
        for col in range(colSize-3):
            line = Board[row, col:col+4]
            utility += evalLine(line, Player, Opponent)

    for col in range(colSize):
        for row in range(rowSize-3):
            line = Board[row:row+4,col]
            utility += evalLine(line, Player, Opponent)

    for row in range(rowSize-3):
        for col in range(colSize-3):
            line = [Board[row+i][col+i] for i in range(4)]
            
            utility += evalLine(line, Player, Opponent)

    for row in range(rowSize-3):
        for col in range(3, colSize):
            line = [Board[row+i][col-i] for i in range(4)]
            utility += evalLine(line, Player, Opponent)
    center_col = len(Board[0]) // 2  
    center_count = sum(Board[row][center_col] == Player for row in range(6))
    utility += center_count 

    return utility

# In[154]:

def MinimaxAlgorithm(Board, depth,Player,colindex):
    opponent=2
    if(Player==1):
        opponent=2
        
    AGentwins=check_goal_test(Board,1)
    if(AGentwins==1):
        return 10000000+depth,Board,colindex
    ComputerWins=check_goal_test(Board,2)
    if(ComputerWins==2):
        return -10000000+depth,Board,colindex
    if(depth==0):
        return UtilityOfBoard(Board,Player,opponent),Board,colindex
    if(Player==1):
        value=float('-inf')
        auxiliaryBoard=None
        children= getAllValidChildren(Board,Player)
        percolindex=10000
        for dicchild in children:
            child=dicchild['childd']
            colindex=dicchild['colindexx']
            # print('child board max',child)
            NewVal,_,_=MinimaxAlgorithm(child, depth-1,2,colindex)

            if(NewVal>value):
                auxiliaryBoard=child
                value=NewVal
                percolindex=colindex
        return value,auxiliaryBoard,percolindex
    else:
        value=float('inf')
        auxiliaryBoard=None
        children= getAllValidChildren(Board,Player)
        for dicchild in children:
            child=dicchild['childd']
            colindex=dicchild['colindexx']
            # print('child board min',child)
            NewVal,_,_=MinimaxAlgorithm(child,depth-1,1,colindex)
            if (NewVal<value):
                auxiliaryBoard=child
                value=NewVal
                percolindex=colindex
        return value,auxiliaryBoard,percolindex


# In[155]:


def alphaBetaPruning(Board, depth,Player,colindex, alpha=float('-inf'), beta=float('inf')):
    opponent=2
    if(Player==1):
        opponent=2
        
    AGentwins=check_goal_test(Board,1)
    if(AGentwins==1):
        return 10000000+depth,Board,colindex
    ComputerWins=check_goal_test(Board,2)
    if(ComputerWins==2):
        return -10000000+depth,Board,colindex
    if(depth==0):
        return UtilityOfBoard(Board,Player,opponent),Board,colindex
    if(Player==1):
        value=float('-inf')
        auxiliaryBoard=None
        children= getAllValidChildren(Board,Player)
        percolindex=10000
        for dicchild in children:
            child=dicchild['childd']
            colindex=dicchild['colindexx']
            # print('child board max',child)
            NewVal,_,_=alphaBetaPruning(child, depth-1,2,colindex,alpha,beta)

            if(NewVal>value):
                auxiliaryBoard=child
                value=NewVal
                percolindex=colindex
            if(beta<=value):
                return NewVal,None,None
            alpha=max(alpha,value)
        return value,auxiliaryBoard,percolindex
    else:
        value=float('inf')
        auxiliaryBoard=None
        children= getAllValidChildren(Board,Player)
        for dicchild in children:
            child=dicchild['childd']
            colindex=dicchild['colindexx']
            # print('child board min',child)
            NewVal,_,_=alphaBetaPruning(child,depth-1,1,colindex,alpha,beta)
            if (NewVal<value):
                auxiliaryBoard=child
                value=NewVal
                percolindex=colindex
                # print(value)
            if(alpha>=value):
                return NewVal,None,None
            beta=min(beta,value)
        return value,auxiliaryBoard,percolindex
       

