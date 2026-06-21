print("Do you have any medical cause?" "Y or N")
medical_cause = str(input())  
if medical_cause=="Y":print("You are allowed to attend exam")
else:
    attendance=int(input())
    if  attendance>=75:
        print("You are allowed")

    else:
        print("Not Allowed")
        






