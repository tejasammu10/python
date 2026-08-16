valid=False

while not valid:
    try:
        n=int(input())
        while n%2==0:
            print("bye")
            n+=1
        valid=True
    except ValueError as ex:
        print(ex,"is Invalid")



    
    










