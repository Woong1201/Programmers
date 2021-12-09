def solution(n, k, cmd):
    answer = ['O'] * n
    hist = []
    p = 0
    for i in cmd:
        if i[0] == 'D':
            p += int(i[2:])
        elif i[0] == 'U':
            p -= int(i[2:])
        else :
            while p > 0:
                k += 1
                if answer[k] == 'O':
                    p -= 1
            while p < 0:
                k -= 1
                if answer[k] == 'O':
                    p += 1
            if i[0] == 'C':
                answer[k] = 'X'
                hist.append(k)
                if 'O' in answer[k:]:
                    k += answer[k:].index('O')
                else :
                    while answer[k] == 'X':
                        k -= 1
            else :
                answer[hist[-1]] = 'O'
                del(hist[-1])

    return ''.join(answer)

n = 8; k = 2
cmd1 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
solution(n, k, cmd1)
solution(n, k, cmd2)
sol1 = "OOOOXOOO"
sol2 = "OOXOXOOO"

#효율성 1-10 실패