def solution(n, k, cmd):
    answer = ['O'] * n
    hist = []
    for i in cmd:
        if i[0] == 'D':
            t = 0
            while t != int(i[2:]):
                k += 1
                if answer[k] == 'O':
                    t += 1
        elif i[0] == 'U':
            t = 0
            while t != int(i[2:]):
                k -= 1
                if answer[k] == 'O':
                    t += 1
        elif i[0] == 'C':
            answer[k] = 'X'
            hist.append(k)
            k2 = k
            while k < n and answer[k] == 'X':
                k += 1
            if k == n:
                k = k2
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

#효율성 6-10 실패