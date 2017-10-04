with open("todo_items_read_test.csv") as f:
    tasks = f.readlines()
    new_tasks = []
    for task in tasks:
        task = task.strip("\n")
        task = task.split("|")
        new_tasks.append(task)

    for task in new_tasks:
        task[1] = task[1].split("-")


print(tasks, new_tasks)
