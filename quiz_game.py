print("welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Lets's Play :)")
Score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    Score = Score + 1
else:
    print("incorrect! Please try again :)")

answer = input("What is the app we use for coding? ")
if answer.lower() == "vs code":
    print('correct!')
    Score = Score + 1
else:
    print("incorrect! Please try again :)")


answer = input("What is green? ")
if answer.lower() == "color":
    print('correct!')
    Score = Score + 1
else:
    print("incorrect! Please try again :)")

print("Total Score is " , Score)