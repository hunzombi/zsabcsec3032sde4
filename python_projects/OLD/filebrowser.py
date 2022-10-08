from array import array
import PySimpleGUI as sg
import os

prev = None
layout = [
    [
        sg.Text("Current Folder"),
        sg.In(size=(50, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
        sg.Button("Home", key="-HOME-"),
        sg.In(size=(15, 1), enable_events=True, key="-SEARCH-"),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(105, 20),
            key="-FILE LIST-",
        ),
    ],
]

window = sg.Window("File Manager", layout)

while True:
    event, value = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-FOLDER-":
        folder = value["-FOLDER-"]
        prev = folder
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        
        window["-FILE LIST-"].update(file_list)
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(value["-FOLDER-"], value["-FILE LIST-"][0])
            if not os.path.isfile(filename):
                window["-FOLDER-"].update(filename)
                folder = filename
                prev = folder
                try:
                    file_list = os.listdir(folder)
                except:
                    file_list = []
                window["-FILE LIST-"].update(file_list)
            else:
                os.system("start "+str(filename))
        except:
            pass
    elif event == "-HOME-":
        window["-FOLDER-"].update("C:/")
        try:
            file_list = os.listdir("C:/")
        except:
            file_list = []
        window["-FILE LIST-"].update(file_list)
    elif event == "-SEARCH-":
        folder = value["-FOLDER-"]
        txte = value["-SEARCH-"]
        arr = []
        for i in os.listdir(folder):
            if str(i).startswith(txte):
                arr.append(i)
        window["-FILE LIST-"].update(arr)


window.close()