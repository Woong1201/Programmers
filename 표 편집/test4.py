def solution(n, k, cmd):
    listO = [i for i in range (n)]
    listw = [0] * n
    hist = []
    p = 0
    for i in cmd:
        if i[0] == 'D':
            p += int(i[2:])
        elif i[0] == 'U':
            p -= int(i[2:])
        else :
            k += p
            p = 0
            if i[0] == 'C':
                hist.append(listO[k])
                for q in range (listO[k]+1, n):
                    listw[q] -= 1
                del(listO[k])
                if k == len(listO):
                    k-=1
            else :
                for q in range (hist[-1]+1, n):
                    listw[q] += 1
                if hist[-1] < listO[k]:
                    k += 1
                listO = listO[:hist[-1]+listw[hist[-1]]]+[hist[-1]]+listO[hist[-1]+listw[hist[-1]]:]
                del(hist[-1])
                
    return ''.join(['O' if i in listO else 'X' for i in range(n)])


n = 8; k = 2
cmd1 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
solution(n, k, cmd1)
solution(n, k, cmd2)
sol1 = "OOOOXOOO"
sol2 = "OOXOXOOO"

#효율성 1-10 실패