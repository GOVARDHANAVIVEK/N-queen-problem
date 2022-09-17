#initialize the board to respective values

def initialize(n,board):
    for key in ['queen','row','col','ltordiagonal','rtoldiagonal']:
        board[key]={}
    for i in range(n):
        board['queen'][i]= -1
        board['row'][i]=0
        board['col'][i]=0
    for i in range(-(n-1),n):
        board['ltordiagonal'][i]=0
    for i in range(2*n-1):
        board['rtoldiagonal'][i]=0
        
def printboard(board):
    for row in sorted(board['queen'].keys()):
        print((row,board['queen'][row]),end=" ")
    print(" ")    
    
def addqueen(i,j,board):
    board['queen'][i]=j
    board['row'][i]=1
    board['col'][j]=1
    board['ltordiagonal'][j-i]=1
    board['rtoldiagonal'][j+i]=1
    
def undoqueen(i,j,board):
    board['queen'][i]=-1
    board['row'][i]=0
    board['col'][j]=0
    board['ltordiagonal'][j-i]=0
    board['rtoldiagonal'][j+i]=0
    
def free(i,j,board):
    return (board['row'][i]==0 and board['col'][j]==0 and board['ltordiagonal'][j-i]==0 and board['rtoldiagonal'][j+i]==0)
    
def placequeen(i,board):
    n = len(board['queen'].keys())
    for j in range(n):
        if free(i,j,board):
            addqueen(i,j,board)
            if i==n-1:
                return True
            else:
                extsol = placequeen(i+1,board)
            if extsol:
                return True
            else:
                undoqueen(i,j,board)
    else:
        return False
        
board={}
n = int(input("enter no of queens: "))
initialize(n,board)        
if placequeen(0,board):
    printboard(board)
    
