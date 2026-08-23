x=int(input())
y=int(input())

def add(x, y):
    result=x+y
    print(result) 
def substract(x, y):
    result=x-y
    print(result)
def multiply(x, y):
    result=x*y
    print(result)
def division(x, y):
    result=x/y
    print(result)

user_operation=(input("+ - / x"))

if user_operation=="+":
    add(x, y)
elif user_operation=="-":
    substract(x, y)
elif user_operation=="/":
    division(x, y)
elif user_operation=="x":
    multiply(x,y)
else:print("INVALID")







