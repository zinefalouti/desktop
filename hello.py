def main():
    first = ask("Hi, what's your name? ")
    second = ask("What's your age? ")
    third = ask("What's your objective? ")
    print(f"Your name is {first}, your age is {second}, and your objective is {third}")
    words = []
    words += first
    words += second
    words += third
    print("_"*30)
    listing(words)
    

def ask(message):
    return input(message)

def listing(list):
    total = len(list)
    print(f"Total str is: {total}")

if __name__ == "__main__":
    main()

