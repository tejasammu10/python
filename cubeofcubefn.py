x=int(input())

def divisible(x):
    if x%3==0:
       return cube(x) 
    else:return "Not divisible"

def cube(x):
    return x**3

y=divisible(x)
print(y)



