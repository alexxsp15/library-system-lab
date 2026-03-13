while True:
    name = input("Enter your name: ")
    if name.strip() == "":
        print("Name cannot be empty. Try again.")
    elif not name.isalpha():
        print("Name must contain only letters. Try again.")
    else:
        print(f"Hello, {name}!")
        print("YO")
        break