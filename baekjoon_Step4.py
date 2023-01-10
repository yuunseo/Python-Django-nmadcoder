'''10807번
Count =int(input())
num=list(map(int,input().split(" ")))
Q = int(input())
print(num.count(Q))'''

'''10871번'''
N, X=map(int,input().split(" "))
num=list(map(int,input().split(" ")))
for i in num:
    if(X>i):
        print(i,end=" ")
        