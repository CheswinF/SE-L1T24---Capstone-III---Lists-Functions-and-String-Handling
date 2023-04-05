#=====importing libraries===========

import datetime 

#login section
team = {}

with open('user.txt','r') as file_main:
    for line in file_main.readlines():
        tokens = line.split(",")            
        team[tokens[0]] = tokens[1].strip()  #assigning stored text file data in different lines
while True:
    user_name = input("Please enter your username: ")
    pass_word = input("Please enter your password: ")

    #if username and password matches - breaks out of loop
    if (password := team.get(user_name)) and password == pass_word:
        break

    else:
        print("Incorrect Username or password, please re-enter")
               
file_main.close()
#space between login and display menu
print()

#functions for menu options
#function to create new user
def reg_user():
    while True:
        
        new_user = input("Enter a new username: ")
        new_user_password = input("Enter a new password: ")
        confirm_new_password = input("Please re-enter your password to confirm: ")

        if new_user_password != confirm_new_password:
            print("Passwords do not macth, Please try again")
            continue
        #checking txt file if username exists
        with open("user.txt","r") as file:
            for line in file:
                if new_user in line:
                    print("User name already exists. Please try again with a different username")
                    break
            #if username is not in txt file - new user will be added to the lsit of users 
            else:
                with open("user.txt","a") as file:
                    file.write(f"\n{new_user},{new_user_password}")
                    print("User successfully registered")
                    break
                    
            file.close()

#function to add new task
def add_task(): 
    task_file = open('tasks.txt','a+')
    
    new_task_username = input("Please enter the USERNAME of the person this task will be asigned to: ")
    new_task_title = input("Please enter the title of the new task: ")
    new_task_description = input("Please enter a brief discprition of new task:\n")
    new_task_date_assigned = input("Please enter the task assignment date:\n")
    new_task_due_date = input("Please enter the due date of the given task in the following format (dd-mm-yyyy):\n")
    new_task_complete = input("Is the new task completed (YES/NO): ")

    #writing new task to text file         
    task_file.write(f"\n{new_task_username}, {new_task_title}, {new_task_description}, {new_task_date_assigned}, {new_task_due_date}, {new_task_complete}")
        
    task_file.close()
print()

#function to view all tasks
def view_all():
    task_file = open("tasks.txt","r")

    #spliting data line and assigning line numbers to variables for output print display
    for line in task_file:

        file_info = line.strip().split(", ")
        new_task_username = file_info[0]
        new_task_title = file_info[1]
        new_task_discription = file_info[2]
        new_task_date_assigned = file_info[3]
        new_task_due_date = file_info[4]
        new_task_complete = file_info[5]
      
        print(f"""------------------------------------------------------------------------
Task:                   {new_task_title}
Assigned to:            {new_task_username}
Date Assigned:          {new_task_date_assigned}
Due Date:               {new_task_due_date}
Task Complete:          {new_task_complete}
Task Discription:       {new_task_discription}
------------------------------------------------------------------------""")
           
    task_file.close()
print()   


#function to view tasks of logged in user
def view_mine():
    tasks =[]
    with open("tasks.txt","r") as file:
        for lines in file:
            task = lines.strip().split(",")
            tasks.append(task)

            #using enumerate to number the tasks                             
            for i, task in enumerate(tasks):
                #check to see if logged user matches the taks assgined to username
                if task[0] == user_name:
                                
                    print(f"""-----------------------------------
{i+1}. User: {task[0]}
Task Title: {task[1]}
Task Discription: {task[2]}
Date Assigned: {task[3]}
Date Due: {task[4]}
Task Complete: {task[5]}
-----------------------------------""")
     
    while True:

        task_num = int(input("Enter the number of task you want to view/edit (-1 to return to main menu): "))   
        if task_num == -1:
            break

        if task_num < 1 or task_num > len(tasks):
            print("invalid task number. Please try again")
            continue

        task = tasks[task_num - 1]
        if task[5] == "Yes":
            print("This task has already been completed and cannot be edited.")
            continue
        edit = int(input("What do you want to do with task? \n1. Edit task\n2. Mark as complete\nEnter number: "))
        if edit == 1:
            username = input("Enter the new username for this task: ")
            duedate = input("Enter the new due date for this task: ")
            task[0] = username
            task[4] = duedate
            print("Task updated successfully")
        elif edit == 2:
            task[5] = "Yes"
            print("Task updated successfully")
        else:
            print("Invalid action. Please try again")
            continue

                
    
    with open("tasks.txt","w") as file:
            for task in tasks:
                file.write(",".join(task)+"\n")

    file.close()            



#function to display total users & total tasks 
def display_stats():
    #Display task_overview.txt data
    with open("task_overview.txt","r") as admin_file:
        task_data = admin_file.readlines()
        print("Task Overview:")
        for line in task_data:
            print(line.strip())

    #Displa user_overview.txt data        
    with open("user_overview.txt","r") as admin_file:
        user_data = admin_file.readlines()
        print("\nUser Overview:")
        for line in user_data:
            print(line.strip())

        
    admin_file.close()

#function to generate reports

def gen_reports():
    
    time  = datetime 
#initialize counters
    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    users = set()
    user_tasks = {}

    #read data from tasks.txt file
    with open("tasks.txt","r") as f:
        data = f.readlines()

        #loop through each line of data
        for line in data:
            task = line.strip().split(",")
            total_tasks +=1
            users.add(task[0])  
            if task[5] == "Yes":
                completed_tasks += 1
            else:
                uncompleted_tasks += 1
                if task[4] < time: 
                    overdue_tasks += 1
            if task[0] in user_tasks:
                user_tasks[task[0]] += 1
            else:
                user_tasks[task[0]]
    
    #Write data to task_overview.txt
    with open("task_overview.txt","w") as f:
        f.write("Total number of tasks: " + str(total_tasks) + "\n")
        f.write("Total number of completed tasks: " + str(completed_tasks) + "\n")
        f.write("Total number of uncompleted tasks: " + str(uncompleted_tasks) + "\n")
        f.write("Total number of overdue tasks: " + str(overdue_tasks) + "\n")
        f.write("Percentage of tasks that are incomplete: " + str(uncompleted_tasks / total_tasks * 100) + "%\n")
        f.write("Percentage of tasks that are overdue: " + str(overdue_tasks / total_tasks * 100) + "%\n")

    # Write data to user_overview.txt
    with open("user_overview.txt", "w") as f:
        f.write("Total number of users: " + str(len(users)) + "\n")
        f.write("Total number of tasks: " + str(total_tasks) + "\n")
        for user in users:
            f.write("\nUser: " + user + "\n")
            f.write("Total number of tasks assigned: " + str(user_tasks[user]) + "\n")
            f.write("Percentage of total tasks assigned: " + str(user_tasks[user] / total_tasks * 100) + "%\n")
            f.write("Percentage of tasks completed: " + str(user_tasks[user] / completed_tasks * 100) + "%\n")
            f.write("Percentage of tasks still to be completed: " + str(user_tasks[user] / (uncompleted_tasks + completed_tasks) * 100) + "%\n")
            f.write("Percentage of overdue tasks: " + str(user_tasks[user] / overdue_tasks * 100) + "%\n") 

#function to exit program 
def exit_prog():
    print('Goodbye!!!')
    exit()

#disply menu options for users (admin or other user)
while True:

    if user_name == "admin":

        #menu option for admin user only 
        menu = input('''Select one of the following Options below:

r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
d - display statistics = Total number of tasks & users
e - Exit
: ''').lower()

    #menu option for all other users
    else:
         menu = input('''\nSelect one of the following Options below:

a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower() 
    #if statements to functions when selection made from menu
    if menu == "r":
        reg_user()
        #print space after function complete to display menu clearer
        print()
    elif menu == "a":
        add_task()
        #print space after function complete to display menu clearer
        print()
    elif menu == "va":
        view_all()
        #print space after function complete to display menu clearer
        print()
    elif menu == "vm":
        view_mine()
        #print space after function complete to display menu clearer
        print()
    elif menu == "d":
        display_stats()
        #print space after function complete to display menu clearer
        print()
    elif menu == "gr":
        gen_reports()
        #print space after function complete to display menu clearer
        print()

    elif menu == "e":
        exit_prog()

    else:
        print("Invalid option. Please try again.")
        #print space after function complete to display menu clearer
        print()