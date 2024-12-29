print('Treasure Hunt: The Legend of the Lost Island\n\n')

print("Chapter 1: The Mysterious Map\n\n")
print("You find an ancient, weathered map in your attic. It's marked with cryptic symbols and an \"X\" on an unknown island. Excited by the prospect of hidden treasure, you decide to embark on an adventure.\n")

ch=int(input("Who do you take with you?\n1]A trusted friend - Someone you know well and can rely on.\n2]An experienced treasure hunter - Someone with a reputation for finding lost treasures. "))

if ch==1:
    print("\nYou decide to take your trusted friend, Alex, with you. Together, you set sail, navigating through turbulent seas towards the mysterious island.")
    print("\n\nChapter 2: The Voyage Begins\n\n")
    print("As you approach the island, you notice it's surrounded by treacherous rocks and strong currents.\n")

    ch=int(input("How do you approach the island?\n1]Steer the ship yourself - You trust your instincts and skills.\n2]Use the lifeboat - It's smaller and more maneuverable in dangerous waters. "))
    if ch==1:
        print("\nYou decide to steer the ship yourself. With Alex's help, you manage to navigate through the rocks and reach the island safely.")
        print("\n\nChapter 3: The Island's Secrets\n\n")
        print("On the island, you find signs of an old civilization and paths leading into the jungle.\n")

        ch=int(input("Which path do you take?\n1]The narrow, winding path - It looks challenging but possibly less traveled.\n2]The wide, clear path - It seems easier but might be more dangerous. "))

        if ch==1:
            print("\nYou and Alex take the narrow, winding path. After hours of trekking, you discover an ancient temple hidden deep in the jungle.\n")
            print("\n\nChapter 4: The Temple's Puzzle\n\n")
            print("Inside the temple, you find a series of puzzles guarding the treasure.\n")

            ch=int(input("How do you solve the puzzles?\n1]Rely on ancient texts - Use the old books and scrolls you found.\n2]Use your intuition - Trust your instincts and intelligence. "))

            if ch==1:
                print("\nUsing the ancient texts, you decipher the puzzles and find the treasure. It's a trove of gold, jewels, and ancient artifacts. You and Alex return home as heroes, rich beyond your wildest dreams.\n")
                print("\nOutcome: Triumph and Treasure\n")

            else:
                print("\nYour intuition leads you astray, and you trigger a trap. You and Alex narrowly escape with your lives but leave the island empty-handed.")
                print("\n\nOutcome: Narrow Escape")
        else:
            print("\nYou and Alex take the wide, clear path. It's easy going at first, but you soon encounter dangerous wildlife and traps. Alex gets injured, and you have to make a tough decision.\n")

            ch=int(input("What do you do?\n1]Press on - Continue towards the treasure.\n2]Turn back - Ensure Alex's safety. "))

            if ch==1:
                print("\nYou press on, but without Alex's help, you struggle to navigate the dangers. You find the treasure but are overwhelmed by traps and creatures. You barely escape with your life, losing the treasure in the process.")
                print("\n\nOutcome: Empty-Handed but Wiser")
            
            else:
                print("\nYou decide Alex's safety is more important and turn back. Though you don't find the treasure, you strengthen your bond with Alex and gain valuable experience for future adventures.")
                print("\n\nOutcome: Narrow Escape")

    else:
        print("\nYou and Alex use the lifeboat. It's a rough journey, but you manage to reach the island's shore safely.")
        print("\n\nChapter 3: The Island's Secrets\n\n\nOn the island, you find signs of an old civilization and paths leading into the jungle.\n")

        ch=int(input("Which path do you take?\n1]The narrow, winding path - It looks challenging but possibly less traveled.\n2]The wide, clear path - It seems easier but might be more dangerous. "))

        if ch==1:
            print("\nYou and Alex take the narrow, winding path. After hours of trekking, you discover an ancient temple hidden deep in the jungle.")
            print("\n\nChapter 4: The Temple's Puzzle\n\n")
            print("Inside the temple, you find a series of puzzles guarding the treasure.\n")

            ch=int(input("How do you solve the puzzles?\n1]Rely on ancient texts - Use the old books and scrolls you found.\n2]Use your intuition - Trust your instincts and intelligence. "))

            if ch==1:
                print("\nUsing the ancient texts, you decipher the puzzles and find the treasure. It's a trove of gold, jewels, and ancient artifacts. You and Alex return home as heroes, rich beyond your wildest dreams.")
                print("\n\nOutcome: Triumph and Treasure")

            else:
                print("\nYour intuition leads you astray, and you trigger a trap. You and Alex narrowly escape with your lives but leave the island empty-handed.")
                print("\n\nOutcome: Narrow Escape")
        else:
            print("\nYou and Alex take the wide, clear path. It's easy going at first, but you soon encounter dangerous wildlife and traps. Alex gets injured, and you have to make a tough decision.")

            ch=int(input("\nWhat do you do?\n1]Press on - Continue towards the treasure.\n2]Turn back - Ensure Alex's safety. "))

            if ch==1:
                print("\nYou press on, but without Alex's help, you struggle to navigate the dangers. You find the treasure but are overwhelmed by traps and creatures. You barely escape with your life, losing the treasure in the process.")
                print("\n\nOutcome: Empty-Handed but Wiser")
            
            else:
                print("\nYou decide Alex's safety is more important and turn back. Though you don't find the treasure, you strengthen your bond with Alex and gain valuable experience for future adventures.")
                print("\n\nOutcome: Narrow Escape")

else:
    print("\nYou decide to take an experienced treasure hunter, Captain Drake, with you. Together, you set sail, navigating through turbulent seas towards the mysterious island.")
    print("\n\nChapter 2: The Voyage Begins\n\n\nAs you approach the island, you notice it's surrounded by treacherous rocks and strong currents.\n")

    ch=int(input("How do you approach the island?\n1]Steer the ship yourself - You trust your instincts and skills.\n2]Let Captain Drake navigate - Trust in his experience and expertise. "))

    if ch==1:
        print("\nYou decide to steer the ship yourself. Despite your best efforts, you misjudge the currents and crash into the rocks. You and Captain Drake are stranded on the island with limited supplies.\n\n\nChapter 3: Survival on the Island\n\n\nYou must find a way to survive and locate the treasure.\n")

        ch=int(input("What do you do first?\n1]Search for food and water - Ensure your basic needs are met.\n2]Look for the treasure - Prioritize finding the treasure. "))

        if ch==1:
            print("\nYou focus on survival, finding fresh water and food. As you explore, you stumble upon clues that lead you to the treasure. With Captain Drake's help, you navigate the island and find the treasure, returning home triumphantly.\n\n\nOutcome: Triumph and Treasure")

        else:
            print("\nYou prioritize finding the treasure, but without sufficient supplies, you and Captain Drake grow weak. You find the treasure but lack the strength to bring it back. You barely escape the island with your lives, leaving the treasure behind.\n\n\nOutcome: Empty-Handed but Wiser")

    else:
        print("\nYou trust Captain Drake's experience. He expertly navigates the ship through the treacherous waters, and you reach the island safely.\n\n\nChapter 3: The Island's Secrets\n\n\nOn the island, you find signs of an old civilization and paths leading into the jungle.\n")

        ch=int(input("Which path do you take?\n1]The narrow, winding path - It looks challenging but possibly less traveled.\n2]The wide, clear path - It seems easier but might be more dangerous. "))

        if ch==1:
            print("\nYou and Captain Drake take the narrow, winding path. After hours of trekking, you discover an ancient temple hidden deep in the jungle.")
            print("\n\nChapter 4: The Temple's Puzzle\n\n")
            print("Inside the temple, you find a series of puzzles guarding the treasure.\n")

            ch=int(input("How do you solve the puzzles?\n1]Rely on ancient texts - Use the old books and scrolls you found.\n2]Use your intuition - Trust your instincts and intelligence. "))

            if ch==1:
                print("\nUsing the ancient texts, you decipher the puzzles and find the treasure. It's a trove of gold, jewels, and ancient artifacts. You and Captain Drake return home as heroes, rich beyond your wildest dreams.")
                print("\n\nOutcome: Triumph and Treasure")

            else:
                print("\nYour intuition leads you astray, and you trigger a trap. You and Captain Drake narrowly escape with your lives but leave the island empty-handed.")
                print("\n\nOutcome: Narrow Escape")
        else:
            print("\nYou and Captain Drake take the wide, clear path. It's easy going at first, but you soon encounter dangerous wildlife and traps. Captain Drake gets injured, and you have to make a tough decision.\n")

            ch=int(input("What do you do?\n1]Press on - Continue towards the treasure.\n2]Turn back - Ensure Captain Drake's safety. "))

            if ch==1:
                print("\nYou press on, but without Captain Drake's help, you struggle to navigate the dangers. You find the treasure but are overwhelmed by traps and creatures. You barely escape with your life, losing the treasure in the process.\n")
                print("\n\nOutcome: Empty-Handed but Wiser\n\n")
            
            else:
                print("\nYou decide Captain Drake's safety is more important and turn back. Though you don't find the treasure, you strengthen your bond with Captain Drake and gain valuable experience for future adventures.")
                print("\n\nOutcome: Narrow Escape")

print("\n\nNo matter the outcome, the adventure leaves a lasting impact on you. You’ve braved unknown seas, explored mysterious lands, and faced formidable challenges. The experience has changed you, making you more resilient and wiser for future endeavors.")


