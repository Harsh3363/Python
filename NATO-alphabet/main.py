import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dic = {word.letter: word.code for (letter, word) in data.iterrows()}

# print(new_dic)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def nato():
    user_name = input("enter any text: ").upper()

    try:
        new_list = [new_dic[letter] for letter in user_name]
    except KeyError:
        print("Sorry only characters allowed")
        nato()
    else:
        # since we can iterate over any sequence using comprehension here we are iterating over a String
        # now for each letter in the string sequence we are passing over the new_dic[letter]
        print(new_list)

nato()
