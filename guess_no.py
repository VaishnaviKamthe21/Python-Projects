import random
logo = '''
   ___                                             _____   _                        _  _                    _                      
  / __|   _  _     ___     ___     ___      o O O |_   _| | |_      ___      o O O | \| |   _  _    _ __   | |__     ___      _ _  
 | (_ |  | +| |   / -_)   (_-<    (_-<     o        | |   | ' \    / -_)    o      | .` |  | +| |  | '  \  | '_ \   / -_)    | '_| 
  \___|   \_,_|   \___|   /__/_   /__/_   TS__[O]  _|_|_  |_||_|   \___|   TS__[O] |_|\_|   \_,_|  |_|_|_| |_.__/   \___|   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
'''
print(logo)

def guess_the_number():
    print("Guess the number between 0 to 100!!")
    difficulty=input("Choose a dificulty. Type 'easy' or 'hard': ").lower()

    if difficulty=='easy':
        attemts=10
    else:
        attemts=5
    
    number=random.randint(0,100)
    chance=attemts
    flag=True
    while attemts!=0:
        print(f"You have {attemts} attempts left!")
        guess= int(input("Enter your guess: "))
        attemts-=1
        if guess==number:
            print(f"You guessed the number in {chance-attemts} attempts!!!")
            flag=False
            break
        elif guess<number:
            print("Too low!")
        elif guess>number:
            print("Too high!!")
    
    if flag:
        print(f"The number was {number}")

    ch=input("Do you want to play again? y/n: ").lower()
    if ch=='y':
        guess_the_number()
    else:
        print("Thank you for playing ^_____^")
        
guess_the_number()