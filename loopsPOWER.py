
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (must be a positive whole number): "))

result = 1
for i in range(exponent):
    result = result * base

print(result)