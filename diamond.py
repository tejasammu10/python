rows=int(input())

for i in range(1,rows+1):
    for j in range(rows-i):

        print(" ",end="")
    number=1
    for j in range(2*i-1):
        print(number,end="")
        number+=1
    print()
for i in range(rows-1,0,-1):
    for j in range(rows-i):

        print(" ",end="")
    number=1
    for j in range(2*i-1):
        print(number,end="")
        number+=1
    print()



