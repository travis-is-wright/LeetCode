"""
Employee class that defines an employee
"""
class Employee:
    def __init__(self, name, age, position, salary: float, start_date: str):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.start_date = start_date
        self.tasks = []

    def formatSalary(self):
        return f"${self.salary:,.2f}"

    def introduction(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old! I have been working "
              f"here since {self.start_date} as a {self.position} making {self.formatSalary()} a year!")

    def assignTask(self, task):
        if self.position.hasAccess(task):
            self.tasks.append(task)
            print(f"{self.name} has been assigned {task.description}")
        else:
            print(f"{self.name} does not have enough clearance to be assigned the task: {task.description}")

    def currentTasks(self):
        res = f"{self.name} current tasks are: "

        for tk in self.tasks:
            res += tk.description + ", "
        print(res)

    def completeTask(self, task):
        for i in range(len(self.tasks)):
            if self.tasks[i] == task:
                self.tasks.pop(i)
                return
        print(f"{self.name} does not have this task: {task.description}")


"""
Task class that defines a task: 
description - description of task
difficulty - difficult of task 
clearance level - the clearance necessary to access task
"""
class Task:
    def __init__(self, description, difficulty, clearance_required = 0):
        self.description = description
        self.difficulty = difficulty
        self.clearance_required = clearance_required

"""
Task Assignment class to manage tasks: 
"""
class TaskAssignment:
    def __str__(self, status):
        self.status = status

    def start(self, task):
        self.status = "Start"

    def inprogress(self, task):
        self.status = "In-progress"

    def complete(self, task):
        self.status = "Completed"

"""
Position class for accessing clearance levels:
"""
class Position:
    def __init__(self, title, description, clearance):
        self.title = title
        self.clearance = clearance

    def __str__(self):
        return self.title

    def hasAccess(self, task: Task):
        return self.clearance >= task.clearance_required

if __name__ == "__main__":
    modify_backend = Task("Modify Backend", 4, 6)
    create_database = Task("Create a database", 1, 7)
    wage_increase = Task("Increase an employees wage", 0, 10)

    software_developer = Position("Software Developer", "Writes and test code", 6)
    data_support_analyst = Position("Data Support Analyst", "Manages and analyzes data", 8)
    administrator = Position("Admin", "Manages entire systems", 10)
    janitor = Position("Janitor", "Cleans the office", 1)

    employee1 = Employee("Gerald Rod", 28, software_developer,
                         100000, "August 10th, 2024" )
    employee2 = Employee("Travis Wright", 23, data_support_analyst,
                         44000, "September 14th, 2024")
    employee3 = Employee("Leslie Perez", 22, administrator, 250000, "May 22nd, 2025")

    employee1.introduction()
    employee2.introduction()

    def employeeAccess(employee, task):
        if employee.position.hasAccess(task):
            return f"{employee.name} HAS access to {task.description}!"
        else:
            return f"{employee.name} DOES NOT have access to {task.description}"

    print(employeeAccess(employee1, modify_backend))
    print(employeeAccess(employee1, wage_increase))
    print(employeeAccess(employee3, wage_increase))

    employee2.assignTask(modify_backend)
    employee2.assignTask(create_database)
    employee2.assignTask(wage_increase)

    employee2.currentTasks()
    employee2.completeTask(modify_backend)
    employee2.currentTasks()