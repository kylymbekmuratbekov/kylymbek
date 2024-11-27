def show_menu():
    print("/nToDo-лист:")
    print("1. Добавить задачу")
    print("2. Удалить задачу")
    print("3. Показать все задачи")
    print("4. Выход")

def add_task(tasks):
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print(f"Задача '{task}' добавлена!")

def delete_task(tasks):
    if not tasks:
        print("Список задач пуст!")
        return
    show_tasks(tasks)
    try:
        task_number = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f"Задача '{removed_task}' удалена!")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Введите корректный номер.")

def show_tasks(tasks):
    if not tasks:
        print("Список")

