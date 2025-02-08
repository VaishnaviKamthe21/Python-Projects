#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open("./Beginner-Python-Projects/Mail Merge Project/Input/Names/invited_names.txt", "r") as names:
    names_list = names.readlines()

with open("./Beginner-Python-Projects/Mail Merge Project/Input/Letters/starting_letter.txt", "r") as letter:
    letter_content = letter.read()

for name in names_list:
    name = name.strip()
    new_letter = letter_content.replace("[name]", name)
    with open(f"./Beginner-Python-Projects/Mail Merge Project/Output/ReadyToSend/Letter_for_{name}.txt", "w") as final_letter:
        final_letter.write(new_letter)
