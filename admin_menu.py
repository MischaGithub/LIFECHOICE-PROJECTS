
# Importing all the option functions from the respective files
from admin_option import add_user, remove_user, show_time_login, show_user_logout

# Import the sys in order to use sys.exit() to return to the main screen
import sys


# Creating a admin menu to be presented to the admin after the login was successful
def admin_menu():

    # A welcome message to be display for the admin
    welcome_message = '\n' + "Welcome Admin!" + '\n'
    welcome_message += "You can choose one of the five options:" + '\n'
    welcome_message += "1: Add user" + '\n'
    welcome_message += "2: Remove user" + '\n'
    welcome_message += "3: Check time_login" + '\n'
    welcome_message += "4: Check time_logout" + '\n'
    welcome_message += "5: Return to main menu" + '\n'
    print(welcome_message)
    # While the program is still running and admin completed a action keep display the menu option
    # Until the admin select to return to the main menu
    running = True
    while running:

        try:
            # The option input
            user_choice = int(input("Please choose option (1,2,3,4,5): "))
            output_message = ""
        except ValueError as err:   # if the selection is anything else but a number it returns this error
            output_message = "ERROR: That was not a valid choice Please try again"
            user_choice = 0

        if user_choice == 1:  # Add user option
            add_user()
        elif user_choice == 2:  # Remove user option
            remove_user()
        elif user_choice == 3:  # Show time login
            show_time_login()
        elif user_choice == 4:  # Show time logout
            show_user_logout()
        elif user_choice == 5:  # Quit the menu option and returning to the main screen
            sys.exit()
        else:
            pass

        print(output_message)


