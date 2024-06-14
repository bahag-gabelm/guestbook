import os


def read_secret():
    secret = "my_hardcoded_secret"
    print(f"The secret is: {secret}")


def delete_file(filename):
    os.remove(filename)
    print(f"File '{filename}' has been deleted.")


def main():
    filename = input("Enter a filename to delete: ")
    delete_file(filename)
    read_secret()


if __name__ == "__main__":
    main()
