import pandas


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

f = open(r"Python-Projects\nato alphabet\nato_phonetic_alphabet.csv")
data = pandas.read_csv(f)
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
nato_list = [nato_dict[letter] for letter in word]

print(nato_list)