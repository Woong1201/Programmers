def solution(n, path, order):
    dic = {}
    for i in range(n):
        dic[i] = [[],[]]
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
            p = route.pop()
            dic[p][0] += route
            for i in route:
                dic[i][1].append(p)
    

    t = 0
    while t != len(order):
        test = order[t]
        if test[0] in dic[test[1]][1]:
            return False
        elif test[0] in dic[test[1]][0]:
            del order[t]
            t -= 1
        t += 1

    o_dic = { i : 0 for i in range(n)}
    while order:
        p = order.pop()
        if o_dic[p[0]] > o_dic[p[1]]:
            return False
        
        p1 = p[0]
        p2 = p[1]
        o_dic[p2] += 1
        
        for i in dic[p1][1]:
            o_dic[i] += 1

        for i in dic[p2][1]:
            o_dic[i] += 1
    
    return True


# n = 9
# path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
# order = [[8,5],[6,7],[4,1]]
# True

# n = 9
# path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
# order = [[4,1],[8,7],[6,5]]
# True

n = 9
path =[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[4,3],[8,7],[6,1]]
False

print(solution(n, path, order))