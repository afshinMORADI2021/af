while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos.append(todo)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
                file.close()
        case 'show' | 'display':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                file.close()
#  new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item=item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of todo to edit :"))
            number= number -1
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            print("here is existing ", todos)

            new_todos = input("new ? :")
            todos[number]=new_todos +'\n'
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number=int(input("number of todos to compete"))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index=number -1
            todos_to_remove = todos[index].strip('\n')

            todos.pop(index)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message= f"todo {todos_to_remove} is removed"
            print(message)

        case 'exit':
            break
        case _:
            print('fuck')
print('Bye')

