name = input("Please enter your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. which way would you like to go? ").lower()

if answer == "left":
    answer = input("You have reched a river you can jump and swim or walk around it type swim for swim and walk for walk around it: ")

    if answer == "swim":
        print("You swam and got eaten by a alligator, YOU LOSE.")
    elif answer == "walk":
        print("you walked into a forest and got hunted by a lion, YOU LOSE.")
    else:
        print("Not a valid option, YOU LOSE.")

elif answer == "right":
    answer = input("you went right, encountered a old wobbley bridge, do you want to cross it or head back, type back for head back and cross for crossing the bridge: ")

    if answer == "back":
        print("You go back and hit by a lightning, YOU LOSE.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to them and they give you gold, YOU WIN! ")
        elif answer == "no":
            print("You do not talk to them they leave, YOU LOSE")
    else:
        print("Not a valid option, YOU LOSE.")    
else:
    print("Not a valid option, YOU LOSE.")    

print("Thank you for Playing", name)






