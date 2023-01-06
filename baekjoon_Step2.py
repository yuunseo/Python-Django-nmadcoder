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

'''9498번'''
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
    print("F")