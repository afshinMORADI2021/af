from script_sec_1 import get_todos, write_todos
import time

#import script_sec_1
#script_sec_1.get_todos()
# from Dir import script_sec_1

now = time.strftime("%b %d, %Y %H: %M :S")
while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or 'new' in user_action:
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)


    elif user_action.startswith("show"):
        todos = get_todos()

#  new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item=item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number= number -1
            todos = get_todos()

            print("here is existing ", todos)

            new_todos = input("new ? :")
            todos[number]=new_todos +'\n'
            write_todos(todos)

        except ValueError:
            print("not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()

            index = number -1
            todos_to_remove = todos[index].strip('\n')

            todos.pop(index)
            write_todos(todos)

            message= f"todo {todos_to_remove} is removed"
            print(message)
        except ValueError:
            print("not valid fuck")
            continue

    elif 'exit' in user_action:
        break
    else :
        print("fuck you")

print('Bye')

