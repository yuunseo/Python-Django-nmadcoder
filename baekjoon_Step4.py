'''10807번
Count =int(input())
num=list(map(int,input().split(" ")))
Q = int(input())
print(num.count(Q))'''

'''10871번
N, X=map(int,input().split(" "))
num=list(map(int,input().split(" ")))
for i in num:
    if(X>i):
        print(i,end=" ")'''

'''10818번
Count = int(input())
num = list(map(int,input().split(" ")))
print(min(num),max(num))'''

'''2562번
num=[]
while(True):
    num.append(int(input()))
    if(len(num)==9):
        break
print(max(num),num.index(max(num))+1)'''

'''5597번
num=[int(input()) for i in range(28)]
for i in range(1,31):
    if(i not in num):
        print(i)'''

'''3052번
result=[]
for i in range(10):
    a = int(input())
    result.append(a%42)
print(len(set(result)))'''

'''1546번
count=int(input())
score = list(map(int,input().split()))

result=[]
for i in range(len(score)):
    result.append(score[i]/max(score)*100)
print(sum(result)/len(result))'''

'''8959번'''
count=int(input())
prob=[]
score=0
num=0
for i in range(count):
    prob.append(input())
for i in prob:
    for j in range(len(i)):
        if(j == 0):
            if(i[j]=="O"):
                num += 1
                score += 1
        elif(j!=0 and i[j]=="O"):
            if(i[j-1]=="O"):
                num+=1
                score+= 1*num
            else:
                num+=1
                score+= 1
        else:
            num = 0
    print(score)
    num=0
    score=0
