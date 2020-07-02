# Creating a user options file
# Import the mysql connector
import mysql.connector


# Creating the register user function
# With the username being unique if the details are incorrect it will return failed to login
def register_user():

    # Displaying a welcome message
    register_message = "Register : Please choose a unique username"
    print(register_message)

    # Connecting to the database LIFECHOICES_ONLINE
    my_database = mysql.connector.connect(host="localhost", user="root", password="1234",
                                      database="LIFECHOICES_ONLINE")

    my_cursor = my_database.cursor()
    # Creating a try catch block to insert database
    # If the username the user enter matches one in the table it will return failed to register user
    # Because no user can have the same username
    try:
        query = "INSERT INTO USER(fullname,username,password) VALUES(%s, %s, %s)"
        user_fullname = str(input("Enter user fullname: \n"))
        user_username = str(input("Enter user name: \n"))
        user_password = str(input("Enter user password: \n"))
        add_user_rec = user_fullname, user_username, user_password
        my_cursor.execute(query, add_user_rec)
        print("Successfully registered user")
    except:
        print("Failed to register user. That username already exist")

    my_database.commit()


def user_login():

    # Displaying a welcome message
    welcome_user_message = "Welcome back! Login please"
    print(welcome_user_message)

    my_database = mysql.connector.connect(host="localhost", user="root", password="1234",
                                      database="LIFECHOICES_ONLINE")

    # Storing my database connection within a variable
    my_cursor = my_database.cursor()

    # Insert the data into the time_login table
    # The reason why I am inserting is for the system to keep track of how many times
    # the user logged in for the day
    # Having a try catch block if the user enters anything else other than the information saved in
    # the database it will deny access and return the message failed to log in
    try:
        query = "INSERT INTO TIME_LOGIN VALUES(%s, %s, now()) "

        username = str(input("Enter username: \n"))
        password = str(input("Enter password: \n"))
        user_rec = username, password
        my_cursor.execute(query, user_rec,)
        print("Successfully logged in")
    except :
        # If the username does not match with what is in the database
        print("Failed to log in! Please make sure your details are correct")

    # Committing to the database the changes
    my_database.commit()


def user_logout():
    # This is just a message to be displayed for this screen
    logout_message = "Logout! Please fill in the required!"
    print(logout_message)

    my_database = mysql.connector.connect(host="localhost", user="root", password="1234",
                                      database="LIFECHOICES_ONLINE")

    # Storing my database connection within a variable
    my_cursor = my_database.cursor()

    # Insert the data into the time_logout table
    # The reason why I am inserting is for the system to keep track of how many times
    # the user logged out for the day
    # Having a try catch block if the user enters anything else other than the information saved in
    # the database it will deny access and return the message failed to log out
    try:
        query = "INSERT INTO TIME_LOGOUT VALUES (%s, %s, now()) "

        username = str(input("Enter username: \n"))
        password = str(input("Enter password: \n"))
        user_rec = username, password
        my_cursor.execute(query, user_rec)
        print("Successfully logged out")
        # Displaying a goodbye message
        goodbye_user_message = "Have a lovely day further"
        print(goodbye_user_message)
    except :
        # If the username does not match with what is in the database
        print("Failed to log out! Please make sure your details are correct")

    # Committing to the database the changes
    my_database.commit()



