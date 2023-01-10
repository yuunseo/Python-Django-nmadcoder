'''2739번
num = int(input())
for i in range(1,10):
    print(f"{num} * {i} = {num*i}")'''

'''10950번
count = int(input())
answer=[]
for i in range(count):
    num1, num2 = input().split()
    answer.append(int(num1)+int(num2))
for i in answer:
    print(i)'''

'''8393번
num = int(input())
for i in range(num-1,0,-1):
    num += i
print(num)'''

'''25304번
total = int(input())
count = int(input())
for i in range(count):
    cost, num = input().split()
    total -= int(cost)*int(num)
if(total == 0):
    print("Yes")
else:
    print("No")'''

'''15552번
import sys
count=int(sys.stdin.readline())
answer=[]
for i in range(count):
    num1, num2 = map(int,sys.stdin.readline().split())
    answer.append(num1+num2)

for i in answer:
    print(i)'''

'''11021번
count = int(input())
answer=[]
for i in range(count):
    num1, num2 = map(int,input().split())
    answer.append(num1+num2)
for i in range(len(answer)):
    print(f"Case #{i+1}: {answer[i]}'''

'''11022번
count = int(input())
answer = [list(map(int, input().split())) for i in range(count)]
for i in range(len(answer)):
    print(f"Case #{i+1}: {answer[i][0]} + {answer[i][1]} = {sum(answer[i])}")'''

'''2438번
count=int(input())
for i in range(count):
    print("*"*(i+1))'''

'''2439번
count = int(input())
for i in range(1,count+1):
    print("{0:>{1}}".format("*"*i,count))'''

'''10952번
a=1
b=1
answer=[]
while(a!=0 and b!=0):
    a,b = map(int,input().split())
    answer.append(a+b)
for i in range(len(answer)-1):
    print(answer[i])'''

'''10951번
while(True):
    try:
        a,b = map(int,input().split())
        print(a+b)
    except:
        break'''

'''1110번'''
num = int(input())
new = num
count = 0
while(True):
    if(new <= 9):
        new = new*10+new
        count += 1
        if(num == new):
            break
    else:
        new = (new%10)*10 + (new//10 + new%10)%10
        count += 1
        if(num == new):
            break
print(count)
