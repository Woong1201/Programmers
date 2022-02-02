def solution(n, path, order):
    dic = {0 : [[],[]]}
    route = [0]
    while route:
        loc = route[-1]
        for i in range(len(path)):
            if loc == path[i][0]:
                route.append(path[i][1])
                del path[i]
                break
            elif loc == path[i][1]:
                route.append(path[i][0])
                del path[i]
                break
        else :
            del route[-1]
        print (route)
        print (dic)

    return True


#n = 9
#path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
#order = [[8,5],[6,7],[4,1]]

n = 9
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[4,1],[8,7],[6,5]]
solution(n, path, order)

y = [[3,4],1,2]
x = [1,2,3,4]
x[-2:]
y.remove(x[-2:])
y
