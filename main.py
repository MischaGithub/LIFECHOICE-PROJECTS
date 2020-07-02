# Importing the files from user_option
from user_options import register_user, user_login, user_logout
# Importing the admin login file
from admin_login import admin_login


# The main screen menu option for users
# This is the main screen function which will always be display to all users
def main():

    welcome_message = '\n' + "Welcome to Life Choices!" + '\n'
    welcome_message += "You can choose one of the three options:" + '\n'
    welcome_message += "1: Login" + '\n'
    welcome_message += "2: Logout" + '\n'
    welcome_message += "3: Register" + '\n'
    # Simply display the menu option for the user
    print(welcome_message)
    # while the program is still running after a option is selected keep display options
    running = True
    while running:
        try:
            # If the option is between 1 and 3 it will display a option accordingly
            user_choice = input("Please choose option (1,2,3): ")

            if user_choice.isdigit():
                user_choice = int(user_choice)
            elif user_choice.isalpha(): # If the user select (a) it take them to a admin login
                user_choice = str(user_choice)
        except ValueError as err:
            output_message = "ERROR: That was not a valid choice! Choose between the follow: 1,2,3."
            user_choice = 0

        if user_choice == 1:
            user_login()    # User login screen
        elif user_choice == 2:
            user_logout()   # User logout screen
        elif user_choice == 3:
            register_user()     # Register user screen
        elif user_choice == 'a':
            admin_login()
        else:
            print("That was not a valid option! Try again")
            main()  # If the selection does not match anyone of the options return message and the menu again


if __name__ == '__main__':
    main()
