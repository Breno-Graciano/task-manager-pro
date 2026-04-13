class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = {
            "title": title,
            "done": False
        }
        self.tasks.append(task)
    
    def list_taks(self):
        return self.tasks
    
    def complete_tasks(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
        def remove_task(self, index):
            if 0 <= index < len(self.tasks):
                self.tasks.pop(index)

from storage import save_data, load_data

class TaskManager:
    def __init__(self):
        # Agora ele já começa carregando o que estava salvo!
        self.tasks = load_data()

    def add_task(self, title):
        task = {"title": title, "done": False}
        self.tasks.append(task)
        save_data(self.tasks) # Salvamento automático

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            save_data(self.tasks) # Salvamento automático

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            save_data(self.tasks) # Salvamento automático           
          
            
