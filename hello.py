def main():
    first = ask("Hi, what's your name? ")
    second = ask("What's your age? ")
    third = ask("What's your objective? ")
    print(f"Your name is {first}, your age is {second}, and your objective is {third}")

def ask(message):
    return input(message)

if __name__ == "__main__":
    main()

