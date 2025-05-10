import pandas

f = open(r"Python-Projects\nato alphabet\nato_phonetic_alphabet.csv")
data = pandas.read_csv(f)
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
try:
    nato_list = [nato_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet please.")
else:
    print(nato_list)