# 
from tabulate import tabulate
import string
import random
import os
import os
from datetime import datetime

# Clear Terminal
def clear_terminal():
    command = "cls" if os.name == "nt" else "clear"
    os.system(command)
clear_terminal()

# Function to take input from user and make password
def pass_creator():
    symbols = "!@#$%^&*()_+[ ]{} ;:.< >?/`~|"
    pas = []
    app = input("Enter name of App or Website you need password for:-")
    upcase = int(input("Enter the number of upper case letters:-"))
    locase = int(input("enter the number of lower case letters:-"))
    num = int(input("enter the number of numbers in the paassword:-"))
    sym = int(input("enter the number of symbols in password:-"))
    for i in range(upcase):
        a = random.choice(string.ascii_uppercase)
        pas.append(a)
    for i in range(locase):
        a = random.choice(string.ascii_lowercase)
        pas.append(a)
    for i in range(num):
        a = str(random.randint(0,9))
        pas.append(a)
    for i in range(sym):
        a = random.choice(symbols)
        pas.append(a)  
    random.shuffle(pas)
    password = "".join(pas)
    return password,app
def list_viewer(filename):
    with open (filename,"r") as file:
                lines = file.readlines()
                data = [line.strip().split(",") for line in lines]
                print(tabulate(data, headers="firstrow", tablefmt="grid"))
# Loop to take input from user to select operation to perform untill user exits
while True: 
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_datetime)
    print("|||  Welcome to password Genetrator  |||")
    print("    1. Create Password and add to a new file")
    print("    2. Create Password and add to an existing file")
    print("    3. View password file")
    print("    4. Retrive Password")
    print("    5. Remove Password from existing file")
    print("    6. Exit")
    op = input("Enter your choice: ")
    
    
    
    # if statement to create new file and save the password and other information to it
    if(op == "1"):
        clear_terminal() 
        
        filename = input("Enter the filename to be created:-") 
        password,app = pass_creator()
        with open(filename,"w") as file:
            file.write("app,password,length,date / time,\n")
            file.write(app+","+password+","+str(len(password))+","+str(formatted_datetime)+"\n")
            print(f"Password saved to {filename}")
        print("\nPassword for "+(app)+" is:- "+(password)+"\n")
        list_viewer(filename)
        print("\n\n")
        
        
    # statement to add data to existing file
    elif(op == "2"):
        clear_terminal() 
        try:
            
            filename = input("Enter the filename to save password:-")
            password,app = pass_creator()
            print("\nPassword for "+(app)+" is:- "+(password)+"\n")    
            with open(filename,"a") as file:
                file.write(app+","+password+","+str(len(password))+","+str(formatted_datetime)+"\n")
                print(f"Password saved to {filename}\n")
            list_viewer(filename)
            print("\n\n")

        except Exception as e:
            print(f"\nAn error occurred: {e}\n")
            
            
            
    # Statement to view the data stored in existing file 
    elif(op == "3"):
        clear_terminal() 
        try:
            filename = input("Enter the filename where passwords are saved:-")
            print("\n")
            list_viewer(filename)
            print("\n")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("\n\n") 
            
            
               
    # statement to retrive password from a password file
    elif(op == "4"):
        clear_terminal() 
        filename = input("Enter file name where password is saved:-")
        try:
            with open(filename, "r") as file:
                name = input("Enter app name to find password: ").lower()
                found = False
                for line in file:
                    row = line.strip().lower()
                    if name in row:
                        app, password,*_ = row.split(",", 3)
                        print(f"\nPassword for {app} is: {password}\n\n")
                        found = True
                        break
                if not found:
                    print("\nApp / website not found in the file.\n")

        except Exception as e:
            print(f"\nAn error occurred: {e}\n")
            
            
            
    # Statement to pop the existing password in the file
    elif op == "5":
        clear_terminal()
        filename = input("Enter file name: ")
        print("\n")
        try:
            pop = input("Enter the password to pop: ").strip()
            password_found = False
            with open(filename, "r") as file:
                lines = file.readlines()
            with open(filename, "w") as file:
                for line in lines:
                    if pop not in line:
                        file.write(line)
                    else:
                        app, password, *_ = line.split(",", 3)
                        password_found = True
            if password_found:
                print(f"\nPassword '{pop}' was popped from {filename}\n")
            else:
                print(f"\nPassword '{pop}' not found in {filename}\n")
            print("UPDATED LIST")
            list_viewer(filename)
            print("\n\n")
        except FileNotFoundError:
            print("\nThe file was not found. Please check the file name and try again.")
        except Exception as e:
            print(f"An error occurred: {e}\n")
            
            
            
    # Statement to exit the while loop
    elif(op == "6"):
        break

    else:
        print("Error: Invalid option. Please try again.") 
        
        