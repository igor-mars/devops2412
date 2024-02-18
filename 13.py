
def insert_names():
    file = open("names.txt", "a")
    for i in range(3):
        file.writelines(input("Write some name") + "\n")
    file.close()


def print_names():
    file = open("names.txt", "r")
    for name in file.readlines():
        print(name, end="")
    file.close()


insert_names()
print_names()
