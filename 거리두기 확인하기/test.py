def solution1(places):
    answer = []
    for i in places:
        n = 1
        for j in range (5):
            for k in range (5):
                if i[j][k] == 'P':
                    if (k <= 3 and i[j][k+1] == 'P') or\
                        (j <= 3 and i[j+1][k] == 'P'):
                        n = 0
                        break
                    if k <= 3 and i[j][k+1] == 'O':
                        if (j >= 1 and i[j-1][k+1] == 'P') or\
                            (k <= 2 and i[j][k+2] == 'P') or\
                            (j <= 3 and i[j+1][k+1] == 'P'):
                                    n = 0
                                    break
                    if k >= 1 and i[j][k-1] == 'O':
                        if (j >= 1 and i[j-1][k-1] == 'P') or\
                            (j <= 3 and i[j+1][k-1] == 'P'):
                                    n = 0
                                    break
                    if j <= 2 and i[j+1][k] == 'O' and i[j+2][k] == 'P':
                        n = 0
                        break
            if n == 0:
                break
        answer.append(n)
    return (answer)

def solution(places):
    answer = []
    for place in places:
        n = 1
        for i in range (5):
            for j in range (5):
                if place[i][j] == 'P' or place[i][j] == 'O':
                    is_P = place[i][j]
                    if i >= 1:
                        is_P += place[i-1][j]
                    if i <= 3:
                        is_P += place[i+1][j]
                    if j >= 1:
                        is_P += place[i][j-1]
                    if j <= 3:
                        is_P += place[i][j+1]
                    if is_P.count('P') >= 2:
                        n = 0
                        break
            if n == 0:
                break
        answer.append(n)
    return (answer)       


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)
