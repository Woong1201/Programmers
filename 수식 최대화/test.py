import itertools
cal = list(itertools.permutations(['+','-','*'],3))

def cal(a, b, c):
    if c == '+':
        return int(a) + int(b)
    elif c == '-':
        return int(a) - int(b)
    else :
        return int(a) * int(b)
        
def solution(expression):
    num = []
    cal = []
    answer = []
    
    i = 0
    for j in range (len(expression)):
        if expression[j].isdigit() == False:
            num.append(expression[i:j])
            cal.append(expression[j])
            i = j + 1
    num.append(expression[i:])
    
    num1 = []
    for i in range(len(cal)):
        if i == '+':
            
            
    return cal


expression = "100-200*300-500+20"

solution(expression)

import re
x=re.split('-', expression)
x
int('3+4')

