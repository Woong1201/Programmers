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
        d1 = direct[1]
        d2 = direct[2]
        if 0<=d0[0][0]<=n and 0<=d0[0][1]<=n\
            and board[d0[0][0]][d0[0][1]]==0:
                #problem
                if dic.get(d0[0],-1)==-1 or dic[d0[0]]>=dic[d0[1]]+100:
                    dic[d0[0]] = dic[d0[1]]+100
                    route.append(d0)
        if 0<=d1[0][0]<=n and 0<=d1[0][1]<=n\
            and board[d1[0][0]][d1[0][1]]==0:
                #problem
                if dic.get(d1[0],-1)==-1 or dic[d1[0]]>=dic[d1[1]]+600:
                    dic[d1[0]] = dic[d1[1]]+600
                    route.append(d1)
        if 0<=d2[0][0]<=n and 0<=d2[0][1]<=n\
            and board[d2[0][0]][d2[0][1]]==0:
                #problem
                if dic.get(d2[0],-1)==-1 or dic[d2[0]]>=dic[d2[1]]+600:
                    dic[d2[0]] = dic[d2[1]]+600
                    route.append(d2)
        
        answer = dic.get((n,n),0)
        del(route[0])
    
    
    return answer