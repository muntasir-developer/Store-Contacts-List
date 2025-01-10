def task_adder():
    tasks = []
    def add_task(task):
        if task not  in tasks:
            tasks.append(task)
            print(f"You have added first task {task}")
        else:
            print("This is available here!")       
    def remove_tasks(task):
        if task in tasks:
            tasks.remove(task)
            print(f"Your task removed {task}")
        else:
            tasks.append(task)
            print(f"Your task successfully added")
    def view_task(task):
        if task in tasks:
            print(f"Your task is available here: {task}")
            print(f"Your all tasks here: {tasks}")
        else:
            print(f"Your task is not available here: {task}")
            print(f"Your all tasks available here: {tasks}")
    
    i = 0
    while True:
        try:
            choice = int(input("For add your task press 1 or\nFor remove the task press 2 and\nFor view the tasks press 3: "))      
            if choice ==1:               
                add_task(input("Enter your task here: "))
            elif choice ==2:
                remove_tasks(input("Enter your task name for remove: "))
            elif choice ==3:
                view_task(input("Enter your task name, and it will show you: "))
            else:
                print("Something went wrong!")            
        except:
            print("Something went wrong! please try again...")    
        i += 1
task_adder()

