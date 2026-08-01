bill_amount=int(input())
tip=int(input())


def total_calc(bill_amount,tip):
    tip_perc=(tip/100)*bill_amount
    total=bill_amount+tip_perc
    print(total)

total_calc(bill_amount,tip)




    
