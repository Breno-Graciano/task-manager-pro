from task_manager import TaskManager

tm = TaskManager()

while True:
    print("\n=== TASK MANAGER PRO ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")

    choice = input("Escolha: ")

    if choice == "1":
        title = input("Digite a tarefa: ")
        tm.add_task(title)

    elif choice == "2":
        tasks = tm.list_tasks()
        for i, t in enumerate(tasks):
            status = "✔" if t["done"] else "❌"
            print(f"{i} - {t['title']} [{status}]")

    elif choice == "3":
        index = int(input("Índice da tarefa: "))
        tm.complete_task(index)

    elif choice == "4":
        index = int(input("Índice da tarefa: "))
        tm.remove_task(index)

    elif choice == "5":
        break 
