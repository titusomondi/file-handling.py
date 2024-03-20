def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1.\n")
            file.write("12345\n")
            file.write("Another line with a mix of strings and numbers.\n")
    except PermissionError:
        print("Permission denied. Unable to create file.")
    except Exception as e:
        print("An error occurred:", e)


def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Content of my_file.txt:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)


def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1.\n")
            file.write("67890\n")
            file.write("Appending line 2.\n")
    except PermissionError:
        print("Permission denied. Unable to append to file.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
    read_file()  # Displaying the file content after appending
