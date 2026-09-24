from math import pi
r = 10
circle_area = pi*r*r
print('circle area:', int(circle_area))


c = 10
f = 1.8*c +32
print(f'{c} = {f}')


from math import sqrt
n = int(input())
if n <= 1:
    print(False)
else:
    prime = True
for i in range(2,int(sqrt(n))+1):
    if n %i == 0:
      prime = False
      break
print(prime)

n = int(input())
sum = 0
for i in range(1,n):
    if (n%i==0):
        sum = sum +i
if (sum == n):
    print('perfect')
else:
    print('not perfect')


list = ['red','blue','green','yellow']
i = input('what is your favorite color:')
if i in list[0:5]:
    print('your color is at',list.index(i),'in my list')
else:
    print(False)


i = [i for i in range(6)]
i1 = [i for i in range(1,11,3)]
i3 = [i-2 for i in range(5)]

print(i,i1,i3)
print(i.sort(reverse=True))
print(i)


def remove_dollar_sign(s):
    h = s.removeprefix('$')
    return h
print(remove_dollar_sign('$hh'))

lst =[1, 4, 5,
-1, 10]
def extract_even(i):
 h = [i for i in lst if i%2==0]
 return h
print(extract_even(lst))


def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
        
    result = 1
    
    for i in range(1, n + 1):
        result *= i
        
    return result
print(calculate_factorial(5))  
print(calculate_factorial(0))  

def all_division(a,b):
    h = a%b
    return h
print(all_division(10,2))

import math
i = lambda x1,y1,x2,y2: sqrt(((x2-x1)**2) + ((y2-y1)**2))
print(i(1,2,3,4))


def htt(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

htt(10, 10)
