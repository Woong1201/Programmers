def solution(n, path, order):
    dic_after = {i:[] for i in range(n)}
    dic_before = {i:[] for i in range(n)}
    route = [0]


    while path:
        p = path.pop()
        dic_after[p[0]] += [p[1]]
        dic_after[p[1]] += [p[0]]
    
    route = [0]
    while route:
        r = route.pop()
        route += dic_after[r]
        for i in dic_before[r]:
            dic_after[i] += dic_after[r]
        
        dic_before[r] += [r]
        for i in dic_after[r]:
            dic_after[i].remove(r)
            dic_before[i] += dic_before[r] 

    
    for i in range(n):
        dic_after[i] = set(dic_after[i])
        dic_before[i] = set(dic_before[i])

    while order:
        o = order.pop()
        
        o0 = o[0]
        o1 = o[1]
        
        if o0 in dic_after[o1]:
            return False
        elif o0 in dic_before[o1]:
            continue
        else:
            for i in dic_before[o0]:
                dic_after[i].add(o1)
                dic_after[i] |= dic_after[o1]
            for i in dic_after[o1]:
                dic_before[i] |= dic_before[o0]
            dic_before[o1] |= dic_before[o0]
        
    
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