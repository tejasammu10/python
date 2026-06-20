a=int(input())
b=int(input())
c=int(input())

avg=(a+b+c)/3
print(avg)

if avg>=(a and b and c):print("It is higher than 'a','b','c'")
elif avg>=(a and b):print("It is higher than 'a','b'")
elif avg>=(a and c):print("It is higher than 'a''c'")
elif avg>=(b and c):print("It is higher than 'b','c'")
elif avg>=(a):print("It is higher than 'a'")
elif avg>=(b):print("It is higher than 'b'")
elif avg>=(c):print("It is higher than 'c'")
else:print("Invalid Input")


