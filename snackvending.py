def calculate_change(paid, price):
    return (paid-price)

snack_price=20
print("Good day sir what would you like?")

print("========= SNACK VENDING MACHINE =========")
print("Snack price is 20 cents only!!")
print("Accepted Coins---  1 , 2 ,5, 10.")

total_inserted=0
coins_inserted=0

while True:
    print("Insert a coin")
    coins=int(input())
    if coins!=1 and coins!=2 and coins!=5 and coins!=10:
        print("Invalid coins! Give Valid coins")
        continue
    total_inserted+=coins
    coins_inserted+=1
    print("total inserted coins", coins_inserted)
    print("total inserted money", total_inserted)
    if total_inserted>=snack_price:
        print("Enough money has been inserted!")
        break

change=calculate_change(total_inserted, snack_price)
print("======= DISPENSING YOUR SNACK =======")

if change==0:pass
else:print("here is your change",change)

print(snack_price)
print(coins_inserted)
print(total_inserted)
print(change)
print("=========THANK YOU FOR BUYING HERE!!=========")




    


