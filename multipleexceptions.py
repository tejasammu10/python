try:
    num1=int(input())
    num2=int(input())

    result=num1/num2

except ZeroDivisionError as ex:
    print("Division by Zero is Error:",ex)

except SyntaxError as e:
    print(e)
except Exception as exe:
    print("Wrong Input")

else:
    print("No Exceptions!")

finally:
    print("This will exectue no matter what!")


















