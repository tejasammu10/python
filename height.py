height=float(input())
weight=float(input())

BMI=weight/(height/100)**2
print(BMI)

if BMI<=18.4:print("undereight")
elif BMI<=24.9:print("healthy")
elif BMI<=29.9:print("over weight")
elif BMI<=34.9:print("severely over weight")
else:print("Obese")


