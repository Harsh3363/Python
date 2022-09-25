replacing_item = "[name]"

with open("./input/Names/invited_names.txt") as name:
    list = name.readlines()
    print(list)

with open("./input/Letters/starting_letter.txt") as Letters:
    Letter_content = Letters.read()
    for name in list:
        name_without_space = name.strip()
        new_letter = Letter_content.replace(replacing_item,name_without_space)
        with open(f"Output/ReadyToSend/{name_without_space}.txt",mode="w") as NL:
            NL.write(new_letter)
