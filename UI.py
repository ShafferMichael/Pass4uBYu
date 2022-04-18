# UI.py

import PySimpleGUI as sg


layout = [
    [sg.Text("Pass4uBYu")],
    [sg.Text("Keyword: ")],
    [sg.Input()],
    [sg.Text("Length: ")],
    [sg.Input()],
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
