def length(a,b):
    return(sum([abs(a[i]-b[i]) for i in range(2)]))

def solution(numbers, hand):
    answer = ''
    dic =[0]
    for i in range(0, 12):
        k = [i // 3, i % 3]
        dic.append(k)

    L = 10
    R = 12
    for i in numbers:
        if i == 0:
            i = 11
        
        if i % 3 == 1:
            ans = 'L'
        elif i % 3 ==0:
            ans = 'R'
        else:
            if length(dic[R], dic[i]) == length(dic[L], dic[i]):
                if hand[0] == 'r':
                    ans = 'R'
                else :
                    ans = 'L'
            elif length(dic[R], dic[i]) > length(dic[L],dic[i]):
                ans = 'L'
            else :
                ans = 'R'
        
        if ans == 'L':
            L = i
        else :
            R = i
        answer += ans
    return answer
            

numbers, hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
solution(numbers, hand)
"LRLLLRLLRRL"