
user_choice = True
user_tasks = []
id_tasks = 0

while user_choice :
  print("--- MENU ---")
  print("1. Criar uma tarefa: ")
  print("2. Excluir uma tarefa: ")
  print("3. Sair ")

  user_task = input("Digite aqui: ")

  

  if(user_task == "3"):
    user_choice = False

  elif user_task == "2":
    print("Digite o id da tarefa")

    id_excluded_task = int(input(": "))

    user_tasks = [t for t in user_tasks if t["id"] != id_excluded_task]
    print(user_tasks)

  elif user_task == "":
   print("A tarefa não pode estar vazia!")


  else:
    id_tasks += 1
    id_tasks = id_tasks
    user_tasks.append({
        "id": id_tasks,
        "task_name": user_task
      })
    print(user_tasks)



else: 
  print("Você saiu do app!")


