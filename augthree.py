
def main():
    name = raw_input("Enter your name: ")
    hello = greeting()
    print hello + name


def greeting():
    return "Hello "


if __name__ == "__main__":
    main()
