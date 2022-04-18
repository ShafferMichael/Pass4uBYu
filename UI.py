# UI.py

import PySimpleGUI as sg

layout = [
        [sg.Image(key="Pass4uBYu")],
        [
            sg.Text("Keyword"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.Text("Length"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.Button("GENERATE"),
        ],
    ]

layout = [
    [sg.Text("Pass4uBYu")],
    [sg.Text("Keyword: ")],
    [sg.Text("Length: ")],
    [sg.Button("GENERATE")]
]

# create the window
window = sg.Window("Pass4uBYu", layout)

# create an event loop
while True:
    event, values = window.read();
    # End program of user closes window
    if event == sg.WINDOW_CLOSED:
        break

    # Press generate button

window.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
