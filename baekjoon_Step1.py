'''	10998번 문제
A,B = input().split()
print(int(A) * int(B))'''

'''1008번 문제
a,b = input().split()
print(int(a)/int(b))'''

'''10869번 문제
a,b = input().split()
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)/int(b))
print(int(a)%int(b))'''

'''10926번 문제
name = input()
print(name+"??!")'''

'''18108번 문제
print(int(input())-543)'''

'''3003번 문제
a,b,c,d,e,f = input().split()
data = ['1','1','2','2','2','8']
num = [a,b,c,d,e,f]
answer = []

Count = 0

for i in data:
    if(num[Count] == i):
        answer.append(0)
    else:
        answer.append(int(i) - int(num[Count]))
    Count += 1

for i in answer:
    print(i,end=' ')'''


'''10430번'''
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c)%c))