def solution(board):
    n = len(board) - 1
    route = [[(1,0),(0,0)], [(0,1),(0,0)]]
    answer = 0
    if board[0][1] == 1:
        dic = {(0,0) : 0, (1,0) : 100}
        route.remove([(0,1),(0,0)])
    elif board[1][0] == 1:
        dic = {(0,0) : 0, (0,1) : 100}
        route.remove([(1,0),(0,0)])
    else :
        dic = {(0,0) : 0, (1,0) : 100, (0,1) : 100}
    
    while len(route)!=0:
        loc = route[0]
        if answer!=0 and dic[loc[0]] > answer:
            del(route[0])
            continue
        
        direct = direction(loc)
        d0 = direct[0]
        if 0<=d0[0][0]<=n and 0<=d0[0][1]<=n\
            and board[d0[0][0]][d0[0][1]]==0:
                #problem
                if dic.get(d0[0],-1)==-1 or dic[d0[0]]>=
                
                
                
                
                
        del(route[0])
        
    return answer

def direction(loc):
    a = loc[0]
    b = loc[1]
    if a[0] - b[0] == 1:
        return [[(a[0]+1,a[1]),a],[(a[0],a[1]+1),a],[(a[0],a[1]-1),a]]
    elif a[0] - b[0] == -1:
        return [[(a[0]-1,a[1]),a],[(a[0],a[1]+1),a],[(a[0],a[1]-1),a]]
    elif a[1] - b[1] == 1:
        return [[(a[0],a[1]+1),a],[(a[0]+1,a[1]),a],[(a[0]-1,a[1]),a]]
    else:
        return [[(a[0],a[1]-1),a],[(a[0]+1,a[1]),a],[(a[0]-1,a[1]),a]]

            
        
        
def solution(board):
    dic = {(0,0) : 0, (1,0) : 100, (0,1) : 100}
    route = [(1,0), (0,1)]
    n = len(board)
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                dic[(i,j)] = -1
    
    answer = 0
    
    while len(route)!=0:
        loc = route[0]
        if answer!=0 and dic[loc]:
            del(route[0])
            continue
        if dic[(loc[0]+1, loc[1]+1)] != -1:
            if dic[(loc[0]+1, loc[1]+1)] > min()
    
a.get('foo', 'bar')
        

board = [[0,0,0],[1,0,0],[0,0,0]]
solution(board)


dic.get((1,0), -1)
a.get('foo', 'bar')