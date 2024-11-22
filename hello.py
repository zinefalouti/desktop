def main():
    first = ask("Hi, what's your name? ")
    second = ask("What's your age? ")
    third = ask("What's your objective? ")
    fourth = ask("Additional comments: ")
    print(f"Your name is {first}, your age is {second}, and your objective is {third}")
    print("-"*6)
    print(f"Comments: {fourth}")
    print(f"Your first name is {first}, your age is {second}, and your objective is {third}")
    words = []
    words += first
    words += second
    words += third
    words += fourth
    print("_"*30)
    listing(words)
    
#Message Function
def ask(message):
    return input(message)

#Listing for STR Length
def listing(list):
    total = len(list)
    print(f"Total str is: {total}")

if __name__ == "__main__":
    main()

