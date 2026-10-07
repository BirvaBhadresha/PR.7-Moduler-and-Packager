def create_file(filename):
    file = open(filename, "w")
    file.close()

    print("File created successfully!")


def write_file(filename):
    data = input("Enter data to write: ")

    file = open(filename, "w")
    file.write(data)
    file.close()

    print("Data written successfully!")


def read_file(filename):
    file = open(filename, "r")
    data = file.read()
    file.close()

    print("\nFile Content:")
    print(data)


def append_file(filename):
    data = input("Enter data to append: ")

    file = open(filename, "a")
    file.write("\n" + data)
    file.close()

    print("Data appended successfully!")