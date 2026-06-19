print("📋 Welcome to To-Do List App!")
# save the tasks into the file 
try:
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file]
except FileNotFoundError:
    tasks = []

while True:
    print("What would you like to do?🤔 ")
    print("1.Add")
    print("2.Remove")
    print("3.View")
    print("4.Clear")
    print("5.Search")
    print("6.Total Tasks")
    print("7.Exit")

    choice = input("Enter your choice: ")

# add the tasks
    if choice == "1":
        new_task = input("Add a new task: ")
        if new_task.strip() == "":
            print("Tasks can't be empty! Please enter a valid task. 🚫")
        elif new_task in tasks:
            print("⚠️ Task already exists! Please enter a different task.")
        else:
            tasks.append(new_task)
            print("✅ Task added successfully!")
            print("Current tasks: ",tasks)

# removed the task 
    elif choice == "2":
        print("removed tasks ")
        removed_tasks = input("enetr task to remove: ")
        if removed_tasks in tasks:
            tasks.remove(removed_tasks)
            print("🗑️tasks removed! ",tasks)
        else:
            print("📪tasks not found")

# view the tasks
    elif choice == "3":
        print("your tasks ",tasks)
        if len(tasks) == 0:
            print("📪No tasks available!")
        else:
            # count the tasks
            print("\n📋 Your Tasks: ")
            count = 1
            for i in tasks:
                print(count,".",i)
                count += 1

# clear all the tasks
    elif choice == "4":
        tasks.clear()
        print("🗑️ All tasks cleared!")  

# search for a task
    elif choice == "5":
        search_task = input("Enter task to search: ")
        if search_task in tasks:
            print("✅ Task found!")
        else:
            print("📪 Task not found")

# Total tasks
    elif choice == "6":
        print("Total tasks: ",len(tasks)) 

# exit the app
    elif choice == "7":
        with open("tasks.txt", "w")as file:
            for task in tasks:
                file.write(task + "\n")
        print("Thanks for using these app😄. Goodbye👋!")
        break

# if user enter invalid option
    else:
        print("🚫Invalid option 🫥 Please choice again! 1,2,3,4,5,6 or 7")
         
