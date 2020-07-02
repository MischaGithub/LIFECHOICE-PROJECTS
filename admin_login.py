# Creating a login page for admin user
# Importing mysql.connector in order to establish a connection to the database
import mysql.connector
# Import the admin menu to be run after the login is successful
from admin_menu import admin_menu


# Creating the admin login function
# With the username being unique if the details are incorrect it will return failed to login
def admin_login():

    # Displaying a welcome message
    welcome_admin_message = "Welcome back Admin!"
    print(welcome_admin_message)

    my_database = mysql.connector.connect(host="localhost", user="root", password="1234",
                                      database="LIFECHOICES_ONLINE")

    # Storing my database connection within a variable
    my_cursor = my_database.cursor()

    # Insert the data into the admin_login table
    # The reason why I am inserting is for the system to keep track of how many times
    # the user logged in for the day
    # Having a try catch block to check if the user is admin
    try:
        # Declaring the query i want to perform
        query = "INSERT INTO ADMIN_LOGIN(username, password, arrival) VALUES (%s, %s, now()) "

        # Admin input
        admin_username = str(input("Enter username: \n"))
        admin_password = str(input("Enter password: \n"))
        # Storing those input in a variable in order to be executed
        admin_rec = admin_username, admin_password

        # If the input from the user is not equal to whats in the database
        # it will denied access to the user
        if admin_username == 'LCAdmin' and admin_password == 'password':
            # Executing all queries
            my_cursor.execute(query, admin_rec)
            print("Successfully logged in")
            admin_menu()
        else:
            print("ACCESS DENIED! Incorrect details please try again")
            admin_login()
    except:
        # If the username does not match with what is in the database
        # If the details are incorrect to return the admin login screen again
        print("Return to main screen")

    # Committing to the database the changes
    my_database.commit()