import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def distribute_hand():
    '''distributes the starting hand'''
    hand=[cards[random.randint(0,12)],cards[random.randint(0,12)]]
    return hand

def take_card(hand):
    '''adds a card to your hand'''
    hand.append(cards[random.randint(0,12)])
    return hand

def display(y_hand,y_score,d_hand,d_score):
    '''Displays final output'''
    print(f"Your final hand: {y_hand}\n Your final score: {y_score}\n")
    print(f"Dealer's final hand: {d_hand}\n Dealer's final score: {d_score}\n")

def ace(score,hand):
    '''selects the value of ace'''
    if score>21 and 11 in hand:
        ind=hand.index(11)
        hand[ind]=1
        return sum(hand)
    else:
        return score

def check(your_score,dealers_score,your_hand,dealers_hand):
    '''checks basic rules'''
    if your_score>21:
        display(your_hand,your_score,dealers_hand,dealers_score)
        print("You went over. You lose ＞︿＜")
        return True
    
    elif dealers_score>21:
        display(your_hand,your_score,dealers_hand,dealers_score)
        print("Dealer went over. You Win! ^0^")
        return True

    elif your_score==21:
        display(your_hand,your_score,dealers_hand,dealers_score)
        print("You won with a Blackjack!! (～￣▽￣)～")
        return True
    
    elif dealers_score==21:
        display(your_hand,your_score,dealers_hand,dealers_score)
        print("You lost! Dealer gets the Blackjack!! T_T")
        return True
    else: 
        return False
    

def final_score(your_score,dealers_score,your_hand,dealers_hand):
    '''compares final score'''
    if your_score==dealers_score:
        display(your_hand,your_score,dealers_hand,dealers_score)
        print("Its a Draw! ~_~")
        return True
    elif your_score>dealers_score:
        display(your_hand,your_score,dealers_hand,dealers_score)
        print("You win!!! (^///^)")
        return True
    elif your_score<dealers_score:
        display(your_hand,your_score,dealers_hand,dealers_score)
        print("You lose..The dealer has a greater hand! X_X")
        return True
    else:
        return False

def blackjack():
    while True:
        gameover=input("Do you want to play a game of Blackjack? 'y' or 'n': ")
        if gameover=='n':
            return 
        your_hand=distribute_hand()
        your_score=ace(sum(your_hand),your_hand)
        print(f"Your Hand: {your_hand}")
        print(f"Your Score: {your_score}")
        dealers_hand=distribute_hand()
        print(f"Dealer's Hand's 1st Card: {dealers_hand[0]}")
        dealers_score=ace(sum(dealers_hand),dealers_hand)

        while True:
            if check(your_score,dealers_score,your_hand,dealers_hand):
                break
            draw=input("Type 'y' to draw a card and 'n' to pass: ")
            if draw=='y':
                your_hand=take_card(your_hand)
                your_score=ace(sum(your_hand),your_hand)
                if check(your_score,dealers_score,your_hand,dealers_hand):
                    break
                
                print(f"Your Hand: {your_hand}")
                print(f"Your Score: {your_score}")
            elif draw=='n':
                while dealers_score<your_score and dealers_score<17:
                    dealers_hand = take_card(dealers_hand)
                    dealers_score=ace(sum(dealers_hand),dealers_hand)
                print(f"Your hand: {your_hand}\n Your score: {your_score}")
                if check(your_score,dealers_score,your_hand,dealers_hand) or final_score(your_score,dealers_score,your_hand,dealers_hand):
                    break
                gameover=input("Do you want to play a game of Blackjack? 'y' or 'n': ")
                if gameover == 'y':
                    break
                else:
                    return




blackjack()