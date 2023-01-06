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

'''14681번
x = int(input())
y = int(input())
if(x>0 and y>0):
    print(1)
elif(x>0 and y<0):
    print(4)
elif(x<0 and y>0):
    print(2)
else:
    print(3)'''

'''2884번
h, m = input().split()
h = int(h)
m = int(m)

if(m >= 45):
    print(h,m-45)
else:
    if(h==0):
        print(23,60-(45-m))
    else:
        print(h-1,60-(45-m))'''

'''2525번'
h,m = map(int,input().split())
t = int(input())

h += t//60
m += t %60

if(m >= 60):
    h += 1
    m -= 60
if(h>=24):
    h -= 24
print(h,m)'''

'''2480번'''
a,b,c = map(int,input().split())
if(a==b==c):
    print(10000+a*1000)
else:
    if(a==b!=c or a==c!=b):
        print(1000+a*100)
    elif(b==c!=a):
        print(1000+b*100)
    else:
        list=[a,b,c]
        print(100*max(list))
