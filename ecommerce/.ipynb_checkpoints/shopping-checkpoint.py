def isSafe(board,row,col,n):
    for i in range(n):
        if board[row][i]=='Q':return False
    for i in range(n):
        if board[i][col] == 'Q': return False
    i=row
    j=col
    while i>=0 and j>=0:
        if board[i][j]=='Q':return False
        i-=1
        j-=1
    i=row
    j=col
    while i>=0 and j<n:
        if board[i][j]=='Q':return False
        i-=1
        j+=1
    return True

def nQueen(board,row,n,ans):
    if row==n:
        ans.append([''.join(r)for r in board])
        return
    for col in range(n):
        if isSafe(board,row,col,n):
            board[row][col]='Q'
            nQueen(board,row+1,n,ans)
            board[row][col]='.'


n=int(input())
board=[['.'for _ in range(n)]for _ in range(n)]
ans=[]
nQueen(board,0,n,ans)

for solution in ans:
    for row in solution:
        print(row)
    print()

