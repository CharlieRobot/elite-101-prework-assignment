print("Welcome to the tech support chatbot")
name = input("Please enter your name: ")
age = int(input("Hello "+ name + ", how old are you? "))

print("Here are the following options you can choose from:\n1. \n2.\n3. \n4. \n5. Exit the conversation.")
the_choice = int(input("Enter the number of your choice: "))
if the_choice == 5:
    print("Thank you for using the chatbot, "+name+". Have a great rest of your day!")
    exit()