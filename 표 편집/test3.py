def solution(n, k, cmd):
    listO = [i for i in range (n)]
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
                del(listO[k])
                if k == len(listO):
                    k-=1
            else :
                if hist[-1] < listO[k]:
                    k += 1
                listO = insert(hist[-1], listO)
                del(hist[-1])

    return ''.join(['O' if i in listO else 'X' for i in range(n)])

def insert(p, A):
    a = -1
    b = len(A)
    c = (a+b)//2
    while b - a > 1:
        if p < A[c]:
            b = c
        else:
            a = c
        c = (a+b)//2
    return A[:c+1] + [p] + A[c+1:]

n = 8; k = 2
cmd1 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
solution(n, k, cmd1)
solution(n, k, cmd2)
sol1 = "OOOOXOOO"
sol2 = "OOXOXOOO"

#효율성 1-10 실패