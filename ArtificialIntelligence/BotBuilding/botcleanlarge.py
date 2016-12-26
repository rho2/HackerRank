def next_move(posr, posc, dimx, dimy, board):
    dr, dc = get_next_dirt(board, dimx, dimy)
    
    if(posc != dc):
        move = (posc < dc) and 'RIGHT' or 'LEFT'
    elif(posr != dr):
        move = (posr < dr) and 'DOWN' or 'UP'
    else:
        move = 'CLEAN'
    print(move)
    
def get_next_dirt(board, x,y):
    for a in range(x):
        for b in range(y):
            if(board[a][b] == 'd'):
                return (a,b)
    
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
