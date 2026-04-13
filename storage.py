import json
import os
FILE_NAME = "tasks.json" 

def save_data(task):
    """Salva a lista de tarefas no arquivo JSON."""
    with open(FILE_NAME, "w", enconding="utf-8") as f:
        json.dump(task, f, indent=4, ensure_ascii=False)

def load_data():
    """Carrega as tarefas do arquivo JSON. Se não existir, retorna lista vazia."""
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, Exception):
        return []