#Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения
# и статус (выполнено/не выполнено). Реализуй функцию для добавления
# задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append({'description':description,
                           'deadline': deadline,
                           'status': 'не выполнено'
                          })

    def comhlete_tasks(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = 'выполнено'
                print(f'Задача {description} выполнена')
            else:
                print(f'Задача {description} не найдена')

    def show_tasks(self):
        print('текущие задачи')
        for task in self.tasks:
            if task['status'] == 'не выполнено':
                print(f'{task['description']} - {task['deadline']} ')


t = Task()
t.add_task('wash the dishes', '20-09-2024')
t.add_task('feed the cat', '20-09-2024')
t.add_task('get delivery', '22-09-2024')
t.add_task('buy the book', '18-09-2024')

t.show_tasks()

t.comhlete_tasks('feed the cat')