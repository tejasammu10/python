def greet_customer():
    print("Welcome")
    print("Lemonade made just for you")

greet_customer()

price=float(input())
cups_sold=int(input())

def calculate_total(price,cups_sold):
    total=price*cups_sold
    return total

total_cost=calculate_total(price,cups_sold)

rounded_total=round(total_cost,2)
print(rounded_total,"Total cost")

amount_paid=float(input())

def calculate_change(paid,total):
    change=paid-total
    return change

change_due=calculate_change(amount_paid,rounded_total)
rounded_change=round(change_due,2)

def thank_you_message_(cups):
    if cups>=5:
        return "Wow Big order, Thank You for ordering here"
    else:
        return "Thanks for stopping by!"
    
closing_message=thank_you_message_(cups_sold)
print(rounded_change)
print(closing_message)

