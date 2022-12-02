def print_menu():
    print("Welcome :)")
    print('1. Display all phone numbers')
    print('2. Add a phone number')
    print('3. Search a phone number')
    print('4. Quit')
    print()

numbers = {}
ch = 0
print_menu()
while True:
    ch = int(input("Select your choice (1-4): "))
    if ch == 1:
        print("Telephone Numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()
        
    elif ch == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone

    elif ch == 3:
        print("Search Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif ch == 4:
        print("Thank You :)")
        break
    
    else:
        print("Enter a valid choice")
