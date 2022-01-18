def solution(n, path, order):
    dic = {0 : 0}
    loc = [0]
    g = 1
    while path:
        loc1 = []
        delete = []
        for i in range(len(path)):
            if path[i][0] in loc:
                loc1.append(path[i][1])
                delete.append(i)
                dic[path[i][1]] = g
            elif path[i][1] in loc:
                loc1.append(path[i][0])
                delete.append(i)
                dic[path[i][0]] = g
        delete.reverse()
        for i in delete:=
            del(path[i])
        g+=1
        loc = loc1
    for i in order:
        if dic[i][1]<
    
    return True

n = 9
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]
solution(n, path, order)