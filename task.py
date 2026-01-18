
user_choice = True
user_tasks = []
id_tasks = 0

while user_choice :
  print("--- MENU ---")
  print("1. Criar uma tarefa: ")
  print("2. Excluir uma tarefa: ")
  print("3. Editar alguma tarefa: ")
  print("4. Ver tarefas ")
  print("5. Sair")

  user_task = input("Digite aqui: ")

  if(user_task == '1'):
   print("Digite sua tarefa:")
   user_task = input(": ")

   id_tasks += 1
   user_tasks.append({
     "id": id_tasks,
     "task_name": user_task
   })

   print(user_tasks)
  
  elif user_task == '2':
    if(len(user_tasks) == 0):
      print("Não há tarefas para excluir.")
    else:
      print(user_tasks) 
      print("Digite o id da tarefa que quer excluir: ")
      id_excluded_task = int(input(": "))

      user_tasks = [t for t in user_tasks if t["id"] != id_excluded_task]
      print("Tarefa excluída com sucesso!")
      print(user_tasks)
    
  elif user_task == '3':
    if (len(user_tasks) == 0):
      print("Não há tarefas para editar.")

    else: 
      print(user_tasks)

      print("Digite o id da tarefa que quer editar:")

      id_update_task = int(input(": "))

      updated_task = input("Edite a nova tarefa: ")

      task_found = [t for t in user_tasks if t["id"] == id_update_task]

      task_found[0]["task_name"] = updated_task

      print("Tarefa atualizada com sucesso!")

      print(task_found)

  elif user_task == '4':
    if(len(user_tasks) == 0):
      print("Não há tarefas para ver")
    else:
      print("Tarefas criadas:")
      print(user_tasks)

  else: 
    user_choice = False
else: 
  print("Você saiu do app!")


