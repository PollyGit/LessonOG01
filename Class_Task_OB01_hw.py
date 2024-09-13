#Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения
# и статус (выполнено/не выполнено). Реализуй функцию для добавления
# задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    all_tasks = []
#    undone_tasks = []

    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status
        Task.all_tasks.append(self)

    def done(self):
        self.status = True

    def __str__(self):
        return f"{self.description}, {self.deadline }, {self.status}"

    @classmethod
    def print_undone(cls):
        for i in cls.all_tasks:
            if i.status == False:
                print(i)

    @classmethod
    def print_all(cls):
        for t in cls.all_tasks:
            print(t)


task1 = Task('wash the dishes', '20-09-2024')
task2 = Task('feed the cat', '20-09-2024')
task3 = Task('get delivery', '22-09-2024')
task4 = Task('buy the book', '18-09-2024')

task4.done()

Task.print_undone()