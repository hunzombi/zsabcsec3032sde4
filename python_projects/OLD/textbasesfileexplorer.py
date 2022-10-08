import os

cur_path = "C:/"

def get_content(path):
    os.listdir(cur_path)

def do_command(commands):
    global cur_path

    if commands[0] == "goto":
        if commands[1][:3] == "C:/":
            cur_path = commands[1]
        else:
            cur_path += commands[1]

    elif commands[0] == "cwd":
        print(cur_path)

    elif commands[0] == "new":
        if cur_path[-1] == '/':
            with open(cur_path+commands[1]) as file:
                file.close()
        else:
            with open(cur_path+'/'+commands[1]) as file:
                file.close()

    elif commands[0] == "clear":
        os.system("cls")

    elif commands[0] == "del":
        x = input(f"Are You Sure you want to delete the file: {cur_path+commands[1]} ?")
        if x == "y":
            os.remove(cur_path+commands[1])
    
    elif commands[0] == "ls":
        try:
            if commands[1] == '-i':
                for file in os.listdir(cur_path):
                    ext = file.split('.')[-1]
                    if ext in ["png", "jpeg", "jpg"]:
                        print(file)
        except:
            for file in os.listdir(cur_path):
                print(file)
    
    else:
        print("Command Not Found!")

while True:
    if not cur_path:
        cur_path = "C:/"
    commands = input(f"{cur_path}-> ").split()
    do_command(commands)