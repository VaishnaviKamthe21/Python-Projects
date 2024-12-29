from art import higher_lower, vs
print(higher_lower)

import random
from game_data import data

def game():
    score=0
    opt1=random.choice(data)
    opt2=random.choice(data)
    while True:
        print(f"Compare A: {opt1['name']}, a {opt1['description']}, from {opt1['country']}")
        print(vs)
        print(f"Compare B: {opt2['name']}, a {opt2['description']}, from {opt2['country']}")

        def compare():
            if opt1['follower_count']==opt2['follower_count']:
                return True
            elif opt1['follower_count']>opt2['follower_count']:
                return 'A'
            else:
                return 'B'

        ans=input("Who has more followers? Type 'A' or 'B': ").upper()

        if ans== compare():
            score+=1
            print(f"You are right!! Current score = {score}")
            opt1=opt2
            opt2=random.choice(data)
        else:
            print(f"You are wrong! Final score= {score}")
            break

game()