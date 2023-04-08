def user_input():
    user=input("enter a sentence")
    return user+'\n'

def read_lines():
    with open('todo.txt', 'r') as file:
        content = file.readlines()
    return content

def write_lines(contentss):
    with open('todo.txt', 'w') as file:
        file.writelines(contentss)