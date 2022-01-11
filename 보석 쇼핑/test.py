def solution(gems):
    dic = {}
    for i in range(len(gems)):
        if gems[i] in dic:
            dic[gems[i]] += [i]
        else :
            dic[gems[i]] = [i]   
    
    gem = set(dic.keys())
    ans = max([i[0] for i in dic.values()]) + 1
    p = ans
    answer = [1, p]
    
    for i in range(1,len(gems) - len(gem) + 1):    
        if dic[gems[i-1]][-1] > i-1:
            if dic[gems[i-1]][dic[gems[i-1]].index(i-1)+1] < p:
                if p - i < ans :
                    ans = p - i
                    answer = [i+1, p]
            else :
                p = p + gems[p:].index(gems[i-1]) + 1
        else :
            break
        
    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
#gems = ["AA", "AB", "AC", "AA", "AC"]
#gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
#gems = ["A","B","B","B","B","B","B","C","B","A"]
solution(gems)