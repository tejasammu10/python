x = input("Enter a single character: ")

if len(x) == 1 and x.isalpha():
    print(f"'{x}' is an alphabet.")
else:
    print(f"'{x}' is not an alphabet.")