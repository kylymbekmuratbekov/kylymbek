import json
import os


# Класс для строительных проектов
class Project:
    def _init_(self, name, deadline, status="В процессе"):
        self.name = name
        self.deadline = deadline
        self.status = status

    def to_dict(self):
        return {"name": self.name, "deadline": self.deadline, "status": self.status}


# Класс для сотрудников
class Employee:
    def _init_(self, name, position):
        self.name = name
        self.position = position

    def to_dict(self):
        return {"name": self.name, "position": self.position}


# Основной класс строительной компании
class ConstructionCompany:
    def _init_(self, data_file="company_data.json"):
        self.projects = []
        self.employees = []
        self.materials = {}
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                data = json.load(file)
                self.projects = [Project(**proj) for proj in data.get("projects", [])]
                self.employees = [Employee(**emp) for emp in data.get("employees", [])]
                self.materials = data.get("materials", {})
        else:
            self.projects = []
            self.employees = []
            self.materials = {}

    def save_data(self):
        with open(self.data_file, "w") as file:
            data = {
                "projects": [proj.to_dict() for proj in self.projects],
                "employees": [emp.to_dict() for emp in self.employees],
                "materials": self.materials,
            }
            json.dump(data, file, indent=4)

    # Управление проектами
    def add_project(self, name, deadline):
        project = Project(name, deadline)
        self.projects.append(project)
        self.save_data()
        print(f"Проект '{name}' добавлен!")

    def list_projects(self):
        if not self.projects:
            print("Нет проектов.")
        else:
            print("\nСписок проектов:")
            for idx, project in enumerate(self.projects, 1):
                print(f"{idx}. {project.name} (Дедлайн: {project.deadline}, Статус: {project.status})")

    def update_project_status(self, name, status):
        for project in self.projects:
            if project.name == name:
                project.status = status
                self.save_data()
                print(f"Статус проекта '{name}' обновлен на '{status}'.")
                return
        print(f"Проект '{name}' не найден.")

    # Управление сотрудниками
    def add_employee(self, name, position):
        employee = Employee(name, position)
        self.employees.append(employee)
        self.save_data()
        print(f"Сотрудник '{name}' добавлен!")

    def list_employees(self):
        if not self.employees:
            print("Сотрудников нет.")
        else:
            print("\nСписок сотрудников:")
            for idx, emp in enumerate(self.employees, 1):
                print(f"{idx}. {emp.name} (Должность: {emp.position})")

    def remove_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                self.save_data()
                print(f"Сотрудник '{name}' удален.")
                return
        print(f"Сотрудник '{name}' не найден.")

    # Управление материалами
    def add_material(self, name, quantity):
        self.materials[name] = self.materials.get(name, 0) + quantity
        self.save_data()
        print(f"Добавлено {quantity} единиц материала '{name}'.")

    def use_material(self, name, quantity):
        if name in self.materials and self.materials[name] >= quantity:
            self.materials[name] -= quantity
            self.save_data()
            print(f"Использовано {quantity} единиц материала '{name}'.")
            if self.materials[name] == 0:
                del self.materials[name]
        else:
            print(f"Недостаточно материала '{name}'.")

    def list_materials(self):
        if not self.materials:
            print("Материалов нет.")
        else:
            print("\nСписок материалов:")
            for name, quantity in self.materials.items():
                print(f"- {name}: {quantity} единиц")


# Интерфейс для пользователя
def main():
    company = ConstructionCompany()

    while True:
        print("\nУправление строительной компанией")
        print("1. Добавить проект")
        print("2. Просмотреть проекты")
        print("3. Обновить статус проекта")
        print("4. Добавить сотрудника")
        print("5. Просмотреть сотрудников")
        print("6. Удалить сотрудника")
        print("7. Добавить материалы")
        print("8. Использовать материалы")
        print("9. Просмотреть материалы")
        print("10. Выход")

        choice = input("Выберите действие (1-10): ")

        if choice == "1":
            name = input("Введите название проекта: ")
            deadline = input("Введите дедлайн проекта (ГГГГ-ММ-ДД): ")
            company.add_project(name, deadline)
        elif choice == "2":
            company.list_projects()
        elif choice == "3":
            name = input("Введите название проекта: ")
            status = input("Введите новый статус проекта: ")
            company.update_project_status(name, status)
        elif choice == "4":
            name = input("Введите имя сотрудника: ")
            position = input("Введите должность сотрудника: ")
            company.add_employee(name, position)
        elif choice == "5":
            company.list_employees()
        elif choice == "6":
            name = input("Введите имя сотрудника для удаления: ")
            company.remove_employee(name)
        elif choice == "7":
            name = input("Введите название материала: ")
            quantity = int(input("Введите количество материала: "))
            company.add_material(name, quantity)
        elif choice == "8":
            name = input("Введите название материала: ")
            quantity = int(input("Введите количество для использования: "))
            company.use_material(name, quantity)
        elif choice == "9":
            company.list_materials()
        elif choice == "10":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "_main_":
    main()





# import json
# import os


# # Класс для строительных проектов
# class Project:
#     def __init__(self, name, deadline, status="В процессе"):
#         self.name = name
#         self.deadline = deadline
#         self.status = status

#     def to_dict(self):
#         return {"name": self.name, "deadline": self.deadline, "status": self.status}


# # Класс для сотрудников
# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     def to_dict(self):
#         return {"name": self.name, "position": self.position}


# # Основной класс строительной компании
# class ConstructionCompany:
#     def __init__(self, data_file="company_data.json"):
#         self.projects = []
#         self.employees = []
#         self.materials = {}
#         self.data_file = data_file
#         self.load_data()

#     def load_data(self):
#         if os.path.exists(self.data_file):
#             with open(self.data_file, "r") as file:
#                 data = json.load(file)
#                 self.projects = [Project(**proj) for proj in data.get("projects", [])]
#                 self.employees = [Employee(**emp) for emp in data.get("employees", [])]
#                 self.materials = data.get("materials", {})
#         else:
#             self.projects = []
#             self.employees = []
#             self.materials = {}

#     def save_data(self):
#         with open(self.data_file, "w") as file:
#             data = {
#                 "projects": [proj.to_dict() for proj in self.projects],
#                 "employees": [emp.to_dict() for emp in self.employees],
#                 "materials": self.materials,
#             }
#             json.dump(data, file, indent=4)

#     # Управление проектами
#     def add_project(self, name, deadline):
#         project = Project(name, deadline)
#         self.projects.append(project)
#         self.save_data()
#         print(f"Проект '{name}' добавлен!")

#     def list_projects(self):
#         if not self.projects:
#             print("Нет проектов.")
#         else:
#             print("\nСписок проектов:")
#             for idx, project in enumerate(self.projects, 1):
#                 print(f"{idx}. {project.name} (Дедлайн: {project.deadline}, Статус: {project.status})")

#     def update_project_status(self, name, status):
#         for project in self.projects:
#             if project.name == name:
#                 project.status = status
#                 self.save_data()
#                 print(f"Статус проекта '{name}' обновлен на '{status}'.")
#                 return
#         print(f"Проект '{name}' не найден.")

#     # Управление сотрудниками
#     def add_employee(self, name, position):
#         employee = Employee(name, position)
#         self.employees.append(employee)
#         self.save_data()
#         print(f"Сотрудник '{name}' добавлен!")

#     def list_employees(self):
#         if not self.employees:
#             print("Сотрудников нет.")
#         else:
#             print("\nСписок сотрудников:")
#             for idx, emp in enumerate(self.employees, 1):
#                 print(f"{idx}. {emp.name} (Должность: {emp.position})")

#     def remove_employee(self, name):
#         for emp in self.employees:
#             if emp.name == name:
#                 self.employees.remove(emp)
#                 self.save_data()
#                 print(f"Сотрудник '{name}' удален.")
#                 return
#         print(f"Сотрудник '{name}' не найден.")

#     # Управление материалами
#     def add_material(self, name, quantity):
#         self.materials[name] = self.materials.get(name, 0) + quantity
#         self.save_data()
#         print(f"Добавлено {quantity} единиц материала '{name}'.")

#     def use_material(self, name, quantity):
#         if name in self.materials and self.materials[name] >= quantity:
#             self.materials[name] -= quantity
#             self.save_data()
#             print(f"Использовано {quantity} единиц материала '{name}'.")
#             if self.materials[name] == 0:
#                 del self.materials[name]
#         else:
#             print(f"Недостаточно материала '{name}'.")

#     def list_materials(self):
#         if not self.materials:
#             print("Материалов нет.")
#         else:
#             print("\nСписок материалов:")
#             for name, quantity in self.materials.items():
#                 print(f"- {name}: {quantity} единиц")


# # Интерфейс для пользователя
# def main():
#     company = ConstructionCompany()

#     while True:
#         print("\nУправление строительной компанией")
#         print("1. Добавить проект")
#         print("2. Просмотреть проекты")
#         print("3. Обновить статус проекта")
#         print("4. Добавить сотрудника")
#         print("5. Просмотреть сотрудников")
#         print("6. Удалить сотрудника")
#         print("7. Добавить материалы")
#         print("8. Использовать материалы")
#         print("9. Просмотреть материалы")
#         print("10. Выход")

#         choice = input("Выберите действие (1-10): ")

#         if choice == "1":
#             name = input("Введите название проекта: ")
#             deadline = input("Введите дедлайн проекта (ГГГГ-ММ-ДД): ")
#             company.add_project(name, deadline)
#         elif choice == "2":
#             company.list_projects()
#         elif choice == "3":
#             name = input("Введите название проекта: ")
#             status = input("Введите новый статус проекта: ")
#             company.update_project_status(name, status)
#         elif choice == "4":
#             name = input("Введите имя сотрудника: ")
#             position = input("Введите должность сотрудника: ")
#             company.add_employee(name, position)
#         elif choice == "5":
#             company.list_employees()
#         elif choice == "6":
#             name = input("Введите имя сотрудника для удаления: ")
#             company.remove_employee(name)
#         elif choice == "7":
#             name = input("Введите название материала: ")
#             try:
#                 quantity = int(input("Введите количество материала: "))
#                 company.add_material(name, quantity)
#             except ValueError:
#                 print("Ошибка: количество должно быть числом.")
#         elif choice == "8":
#             name = input("Введите название материала: ")
#             try:
#                 quantity = int(input("Введите количество для использования: "))
#                 company.use_material(name, quantity)
#             except ValueError:
#                 print("Ошибка: количество должно быть числом.")
#         elif choice == "9":
#             company.list_materials()
#         elif choice == "10":
#             print("Выход из программы. До свидания!")
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")


# if __name__ == "__main__":
#     main()
