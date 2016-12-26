#!/bin/python3
def nextMove(posr, posc, board):
    dr, dc = get_next_dirt(board)
    
    if(posc != dc):
        move = (posc < dc) and 'RIGHT' or 'LEFT'
    elif(posr != dr):
        move = (posr < dr) and 'DOWN' or 'UP'
    else:
        move = 'CLEAN'
    print(move)
    
def get_next_dirt(board):
    for a in range(5):
        for b in range(5):
            if(board[a][b] == 'd'):
                return (a,b)

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
