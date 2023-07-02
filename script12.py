todos = []
while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo =input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            print(todos)
            for index, item in enumerate(todos):
                row=f"{index +1}-{item}"
                print (row)
        case 'edit':
            number = int(input("Number of todo to edit :"))
            number= number -1
            new_todos = input("new ? :")
            todos[number]=new_todos
        case 'complete':
            number = int(input("Number of todo to complete:"))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print('fuck')
print('Bye')