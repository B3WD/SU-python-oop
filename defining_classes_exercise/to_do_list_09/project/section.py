# from task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        matching_task = [existing_task for existing_task in self.tasks if existing_task.name == task.name]
        if matching_task:
            return f"Task is already in the section {self.name}"

        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name):
        matching_task = [existing_task for existing_task in self.tasks if existing_task.name == task_name]
        if matching_task:
            task_to_complete = matching_task[0]
            task_to_complete.completed = True
            return f"Completed task {task_to_complete.name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_count = 0
        for task in self.tasks:
            if task.completed:
                removed_count += 1
                self.tasks.remove(task)

        return f"Cleared {removed_count} tasks."

    def view_section(self):
        info = f"Section {self.name}:\n"
        for task in self.tasks:
            info += f"{task.details()}\n"

        return info


# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())