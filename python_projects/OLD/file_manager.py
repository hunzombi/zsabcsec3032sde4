import PySimpleGUI as sg
import os

# 2 column window layout

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20),
            key="-FILE LIST-"
        )
    ],
]

# showing the name of the choosen files

image_viewer_column = [
    [sg.Text("Choose an image from the list on the left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# Final Layout

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window(title="Image Viewer", layout=layout)

# event loop

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    # make a list of files

    if event == "-FOLDER-":
        folder = value["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]

        window["-FILE LIST-"].update(fnames)
    
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
            value["-FOLDER-"], value["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass


window.close()