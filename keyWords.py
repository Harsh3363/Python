try:
    file = open("filename.txt")
    dic = {"key": "value"}
    print(dic["vrvrw"])

except FileNotFoundError:
    file = open("filename.txt", "w")
    file.write("Something to be written inside the file")

# trying to catch the error =>
except KeyError as error_message:
    print(f"the error is {error_message}")
# if programs runs without any error then the else block will run =>
else:
    print("no error occurred")
# this will run everytime even if errors are there or not =>
finally:
    file.close()
    print("file has been closed")
