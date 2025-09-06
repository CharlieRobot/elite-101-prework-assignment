print("Welcome to the tech support chatbot!")
name = input("Please enter your name: ")
age = int(input("Hello "+ name + ", how old are you? "))
def myAge(age):
    if age <15:
        print("\nWelcome! You're a young fella!\n")
    if age >=15<17:
        print("\nI wish I was in high school again... how may I help you?\n")
    if age >=18<55:
        print("\nNot too old yet.. how may I help you?\n")
    if age >=55<120:
        print("\nWow! Good job taking care of yourself and living. Welcome! How may I help you?\n")
    if age >=120:
        print("\nI don't think anyone living is that age right now.. but whatever.\n")

myAge(age)
while True:
    print("Here are the following options you can choose from:\n1. Placeholder 1 \n2. Placeholder 2\n3. Placeholder 3\n4. Placeholder 4 \n5. Exit the conversation.")
    the_choice = int(input("Enter the number of your choice: "))
    if the_choice == 1:
        print("\nWhen there is something here, I will tell you the answer to the problem you selected.\n")
    if the_choice == 2:
        print("\nWhen there is something here, I will tell you the answer to the problem you selected.\n")
    if the_choice == 3:
        print("\nWhen there is something here, I will tell you the answer to the problem you selected.\n")
    if the_choice == 4:
        print("\nWhen there is something here, I will tell you the answer to the problem you selected.\n")
    if the_choice == 5:
        print("\nThank you for using the chatbot, "+name+". Have a great rest of your day!")
        exit()