
number = int(input())
temp_number = number

if temp_number < 0:
    temp_number = -temp_number

if temp_number == 0:
    count = 1
else:
    count = 0
    while temp_number > 0:
        temp_number = temp_number // 10  
        count += 1                       

print(f"The number of digits is: {count}")