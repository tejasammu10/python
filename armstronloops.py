num=int(input())
sum=0
temp=num

while num>0:
    digit=num%10
    sum=digit**3+sum
    num=num//10 

if temp==sum:print("num" "is an amstrong number")
else:print("It is not an amstrong number")






    



# 2) Set `sum` to 0.
#    (This will store the total of the cubes of each digit.)

# 3) Copy `num` into `temp`.
#    (We will change `temp` while checking digits, but we must keep `num` unchanged.)

# 4) Repeat while `temp` is greater than 0:
#    a) Find the last digit of `temp` and store it in `digit`.
#    b) Add (digit × digit × digit) to `sum`.
#    c) Remove the last digit from `temp` so you can move to the next digit.

# 5) After the loop, compare `num` and `sum`:
#    - If they are the same, print: `num` is an Armstrong number.
#    - Otherwise, print: `num` is not an Armstrong number.