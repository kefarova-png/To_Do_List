import time


class ToDoList:
    def __init__(self):
        self.tasks = []  #  Инициализируем список задач как список словарей: {'task': название, 'time': время_создания, 'done': статус}


    def add_task(self, task):
        from datetime import datetime
        current_time = datetime.now()
        self.tasks.append({'task': task, 'time': current_time, 'done': False})  #  Добавляем словарь (новую задачу) со статусом 'не выполнена' (False)


    def complete_task(self, task):
        for t in self.tasks:  #  Ищем задачу по названию и помечаем как выполненную
            if t['task'] == task:
                t['done'] = True
                break
        else:  #  Название задачи не найдено
            print(f"Задача '{task}' не существует.")


    def remove_task(self, task):
        for t in self.tasks:  #  Ищем (по названию) и удаляем задачу
            if t['task'] == task:
                self.tasks.remove(t)
                break
        else:
            print(f"Задача '{task}' не существует.")


    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")  #  Если нет задач
            return
        for t in self.tasks:  #  Перебираем поля задач
            status = "[✓]" if t['done'] else "[×]"  #  Значок статуса в зависимости от "истинности" t['done']
            time_to_print = t['time'].strftime("%Y-%m-%d %H:%M:%S")  #  Отображаемое время
            print(f"{t['task']} (от {time_to_print}) {status}")  #  Выводим список названий задач со значками


#  Проверка
print('\nСозданы две задачи с интервалом 2 секунды\n')
todo = ToDoList()
todo.add_task("Задача 1")
time.sleep(2)
todo.add_task("Задача 2")
todo.list_tasks()
print('\nЗадача 1 - завершена\n')
todo.complete_task("Задача 1")
todo.list_tasks()
print('\nЗадачи 2 - удалена\n')
todo.remove_task("Задача 2")
todo.list_tasks()
print('\nЗадачи 1 - удалена\n')
todo.remove_task("Задача 1")
todo.list_tasks()