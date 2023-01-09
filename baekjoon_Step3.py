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

'''25304번'''
total = int(input())
count = int(input())
for i in range(count):
    cost, num = input().split()
    total -= int(cost)*int(num)
if(total == 0):
    print("Yes")
else:
    print("No")