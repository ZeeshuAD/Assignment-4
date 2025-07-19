data = input("Enter some text to write into the file: ")
with open("output.txt", "w") as file:
    file.write(data + "\n")

more_data = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(more_data + "\n")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
