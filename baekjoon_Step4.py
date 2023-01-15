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

'''3052번'''
result=[]
for i in range(10):
    a = int(input())
    result.append(a%42)
print(len(set(result)))