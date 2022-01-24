def solution(n, path, order):
    route = {0:0}
    for i in path:
        if i[0] in route:
            route[i[0]] += 1
        else :
            route[i[0]] = 0
        if i[1] in route:
            route[i[1]] += 1
        else :
            route[i[1]] = 0
    loc = {0 : 0}
    loc1=[0]
    p = 1
    
    while path:
        path1 = path
        while route[loc1[-1]]!=0:
            for i in range(len(path1)):
                if loc1[-1] == path1[i][0]:
                    loc1.append(path1[i][1])
                    loc[path1[i][1]] = p
                    del(path1[i])
                    p+=1
                    break
                elif loc1[-1] == path1[i][1]:
                    loc1.append(path1[i][0])
                    loc[path1[i][0]] = p
                    del(path1[i])
                    p+=1
                    break
                
        order1 = []
        while order:
            o = order.pop()
            if loc.get(o[0],-1) > loc.get(o[1],200000):
                return False
            elif loc.get(o[0],-1)!=-1 or loc.get(o[1],-1)!=-1:
                continue
            order1.append(o)
        order = order1
        
        while path:
            del(loc[loc1[-1]])
            for i in path:
                if i[0] == loc1[-1] or i[1] == loc1[-1]:
                    path.remove(i)
                    break
            del(loc1[-1])
            route[loc1[-1]]-=1
            if route[loc1[-1]]!=0:
                break
            p-=1
            
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
