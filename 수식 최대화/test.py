import itertools
per = list(itertools.permutations(['+','-','*'],3))

def cal(num, cal, sign):
    num1 = num
    cal1 = []
    
    for s in sign:
        cal1 = []
        i = 0
        k = -1
        
        for j in range(len(cal)):
            if cal[j] == s:
                num1 = num1[0:i] + [eval(str(num1[i]) + s + str(num1[i+1]))] + num1[i+2:]
                cal1 += cal[k+1:j]
                k = j
                i-=1
            i+=1

        cal1 += cal[k+1:]
        cal = cal1

    
    return abs(num1[0])

def solution(expression):
    answer = []
    num=[]
    c=[]
    
    i = 0
    for j in range (len(expression)):
        if expression[j].isdigit() == False:
            num.append(expression[i:j])
            c.append(expression[j])
            i = j + 1
    num.append(expression[i:])
    
    for p in per:
        answer.append(cal(num,c,p))
            
            
    return max(answer)


expression = "100-200*300-500+20"
solution(expression)



def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            print(temp)
            temp_list.append(f'({b.join(temp)})')
            print(temp_list)
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)