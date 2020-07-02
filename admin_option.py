# Creating option for admin to add, remove user
# To also give the admin an option to check the time logs
# Importing mysql.connector
import mysql.connector


# Creating a add user function for the admin
def add_user():

    # The database connection
    my_database = mysql.connector.connect(host="localhost", user="LCAdmin",
                                          password="password", database="LIFECHOICES_ONLINE")

    my_cursor = my_database.cursor()

    # Try catch block for the input of the user
    # Having the required fields for the user to be filled in
    try:
        query = "INSERT INTO USER(fullname,username,password) VALUES(%s, %s, %s)"
        user_fullname = str(input("Enter user fullname: \n"))
        user_username = str(input("Enter user name: \n"))
        user_password = str(input("Enter user password: \n"))
        add_user_rec = user_fullname, user_username, user_password
        my_cursor.execute(query, add_user_rec)  # If the user details inserted correctly print the success message
        print("Successfully added user")
    except:
        # If the data was not insert return the message below
        print("Failed to add user")

    my_database.commit()


def remove_user():

    # Database connection
    my_database = mysql.connector.connect(host="localhost", user="LCAdmin",
                                          password="password", database="LIFECHOICES_ONLINE")

    my_cursor = my_database.cursor()
    # Create a variable for the admin to enter the username to be deleted
    username_delete = str(input("Enter username: \n"))

    # The Reason why i have 3 Try catch blocks to run the query successful and remove the user
    # If not display failed remove user
    try:
        query = "Delete FROM TIME_LOGOUT where username = '" + username_delete + "'"

        my_cursor.execute(query)
        print("Successfully remove the user from TIME_LOGOUT")
        for user in my_cursor:
            print(user)
    except:
        print("Failed to delete user from TIME_LOGOUT!")

    my_database.commit()

    try:
        query = "Delete FROM TIME_LOGIN where username = '" + username_delete + "'"

        my_cursor.execute(query)
        print("Successfully remove the user from TIME LOGIN")
        for user in my_cursor:
            print(user)
    except:
        print("Failed to delete user from TIME_LOGIN!")

    my_database.commit()

    try:
        query = "Delete FROM User where username = '" + username_delete + "'"

        my_cursor.execute(query)
        print("Successfully remove the user from USER")
        for user in my_cursor:
            print(user)
    except:
        print("Failed to delete user from USER")

    my_database.commit()


def show_time_login():

    # Database connection
    my_database = mysql.connector.connect(host="localhost", user="LCAdmin",
                                          password="password", database="LIFECHOICES_ONLINE")

    my_cursor = my_database.cursor()

    # In order for the admin to kept track of all the logs for the day
    user_login = "SELECT * FROM TIME_LOGIN"

    my_cursor.execute(user_login)

    # For all the logs display them sep by (-)
    for users in my_cursor:
        print(*users, sep=" - ")


def show_user_logout():

    # Database connection
    my_database = mysql.connector.connect(host="localhost", user="LCAdmin",
                                          password="password", database="LIFECHOICES_ONLINE")

    my_cursor = my_database.cursor()

    # To keep track of all the logout of every user
    user_login = "SELECT * FROM TIME_LOGOUT"

    my_cursor.execute(user_login)
    #  For all the logs display them by (-)
    for users in my_cursor:
        print(*users, sep=" - ")


















