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
        else:
            t += 1


    while order:
        p = order.pop()
        
        p0 = p[0]
        p1 = p[1]
        
        if p0 in dic[p1][1]:
            return False
        elif p0 in dic[p1][0]:
            continue
        else:
            dic_p0 = dic[p0][0]
            for i in range(len(dic_p0)):
                if dic_p0[i] != (dic[p1][0]+[p1])[i]:
                    dic_p0 = dic_p0[i:] + [p0]
                    break
            
            for i in dic_p0:
                dic[i][1] += [p1] + dic[p1][1]
            for i in dic[p1][1]+[p1]:
                dic[i][0] += [p0] + dic[p0][0]
        
    
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

#효율성 실패
#018 012 036 074 075