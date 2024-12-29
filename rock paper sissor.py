import random
rock='''
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
sissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options=[rock,paper,sissor]

user_ch=int(input("Enter your choice: \n1] Rock \n2] Paper \n3] Sissor \n"))

comp_ch=random.randint(1,len(options))

print("You picked: \n"+options[user_ch-1])

print("Computer picked: \n"+options[comp_ch-1]+"\n\n")

if user_ch==1:
    if comp_ch==1:
        print("Its a Draw")
    elif comp_ch==2:
        print("You Lose!!")
    else:
        print("You WIN!!!!")
elif user_ch==2:
    if comp_ch==2:
        print("Its a Draw")
    elif comp_ch==3:
        print("You Lose!!")
    else:
        print("You WIN!!!!")
elif user_ch==3:
    if comp_ch==3:
        print("Its a Draw")
    elif comp_ch==1:
        print("You Lose!!")
    else:
        print("You WIN!!!!")