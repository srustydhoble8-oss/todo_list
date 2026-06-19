print("📋 Welcome to To-Do List App!")
tasks = input("enter the task: ").split(",")
print(tasks)
while True:
    print("What would you like to do?🤔 ")
    print("1.Add")
    print("2.Remove")
    print("3.view")
    print("4.Clear")
    print("5.Search")
    print("6.Exit")

    choice = input()

    if choice == "1":
        new_task = input("Add a new task: ")
        if new_task not in tasks:
            tasks.append(new_task)
            print("✅ Task added successfully!")
            if new_task.strip() == "":
                print("⚠️ Task cannot be empty!")
        else:
            print("⚠️ Task already exists!")
    elif choice == "2":
        print("removed tasks ")
        removed_tasks = input("enetr task to remove: ")
        if removed_tasks in tasks:
            tasks.remove(removed_tasks)
            print("🗑️tasks removed! ",tasks)
        else:
            print("📪tasks not found")
    elif choice == "3":
        print("your tasks ",tasks)
        if len(tasks) == 0:
            print("📪No tasks available!")
        else:
            # count the tasks
            print("/n📋 Your Tasks: ")
            count = 1
            for i in tasks:
                print(count,".",i)
                count += 1
    elif choice == "4":
        tasks.clear()
        print("🗑️ All tasks cleared!")            
    elif choice == "5":
        search_task = input("Enter task to search: ")
        if search_task in tasks:
            print("✅ Task found!")
        else:
            print("📪 Task not found")
    elif choice == "6":
        print("Thanks for using these app😄. Goodbye👋!")
        break
    else:
        print("🚫Invalid option 🫥 Please choice again! 1,2,3,4,5 or 6")
         
