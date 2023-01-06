'''1330번
a,b = input().split()
a = int(a)
b = int(b)
if(a<b):
    print("<")
elif(a>b):
    print(">")
else:
    print("==")'''

'''9498번
score = int(input())
if(score>=90):
    print("A")
elif(score>=80):
    print("B")
elif(score>=70):
    print("C")
elif(score>=60):
    print("D")
else:
    print("F")'''

'''2753번
year =int(input())
if(year%4==0 and (year%100 != 0 or year%400 == 0)):
    print(1)
else:
    print(0)'''

'''14681번'''
x = int(input())
y = int(input())
if(x>0 and y>0):
    print(1)
elif(x>0 and y<0):
    print(4)
elif(x<0 and y>0):
    print(2)
else:
    print(3)