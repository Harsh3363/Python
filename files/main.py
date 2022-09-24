with open("main.txt", mode="r") as file:
    contents = file.read()
    print(contents)

with open("main.txt", mode="a") as file:
    file.write("\n this is the new line added")
    print(contents)
