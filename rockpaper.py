import random

while True:
    user_action=str(input("rock,paper,scissor"))
    possible_actions=["rock","paper","scissor"]
    computer_action=random.choice(possible_actions)

    print("These  are the choices", "user action:", user_action, "computer action:", computer_action)

    if computer_action==user_action:
        print("TIE!")
    elif (user_action=="rock" and computer_action=="scissor") or (user_action=="scissor" and computer_action=="paper") or (user_action=="paper" and computer_action=="rock"):
        print("You have WON!")
    else:
        print("You Lost")
    print("want another try??","Y or N")
    x=input()
    if x=="N": break


    


