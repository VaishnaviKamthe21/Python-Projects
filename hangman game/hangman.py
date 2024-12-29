import words
import random

def draw_hangman(lives):
    stages = [
        """
         _______
        |/    |
        |     
        |    
        |   
        |
        """,
        """
         _______
        |/    |
        |     O
        |    
        |   
        |
        """,
        """
         _______
        |/    |
        |     O
        |     |
        |   
        |
        """,
        """
         _______
        |/    |
        |     O
        |    /|
        |   
        |
        """,
        """
         _______
        |/    |
        |     O
        |    /|\\
        |   
        |
        """,
        """
         _______
        |/    |
        |     O
        |    /|\\
        |    /
        |
        """,
        """
         _______
        |/    |
        |     O
        |    /|\\
        |    / \\
        |
        """
    ]
    
    return stages[lives]


word=words.hangman_words[random.randint(0,len(words.hangman_words)-1)]
dashed_word=["_"]*len(word)
lives=0
print("Welcome to Hangman!")
print(' '.join(dashed_word))
print(draw_hangman(lives))

while True:
    ip=input("Enter a letter: ")
    if ip in word:
        for i in range(len(word)):
            if word[i]==ip:
                dashed_word[i]=ip
        print(' '.join(dashed_word))
        print(draw_hangman(lives))
        
    elif ip not in word:
        #draw hangman
        lives+=1
        print(' '.join(dashed_word))
        print(draw_hangman(lives))

    if ''.join(dashed_word)==word:
        print("You found the word and saved the man!!")
        break

    if lives==6:
        print("Oops! The man was killed")
        print(word)
        break
