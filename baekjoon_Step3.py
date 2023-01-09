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

'''11021번'''
count = int(input())
answer=[]
for i in range(count):
    num1, num2 = map(int,input().split())
    answer.append(num1+num2)
for i in range(len(answer)):
    print(f"Case #{i}: {answer[i]}")