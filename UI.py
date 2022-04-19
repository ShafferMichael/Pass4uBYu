import PySimpleGUI as sg
import main

layout = [
    [sg.Text("Pass4uBYu", font=("Helvetica", 25))],
    [sg.Text("Keyword: ", font=("Helvetica", 15))],
    [sg.InputText()],
    [sg.Text("Length: ", font=("Helvetica", 15))],
    [sg.InputText()],
    [sg.Button("GENERATE", font=("Helvetica", 15))],
    [sg.Output()]
]

# create the window
window = sg.Window("Pass4uBYu", layout, element_justification='c')

# create an event loop
while True:
    event, values = window.read()
    # End program of user closes window
    if event == sg.WINDOW_CLOSED:
        break

    # Press generate button
    if event == "GENERATE":
        # Print from main variable
        for values in main.topPasswords.items():
            print(main.topPasswords[values])

window.close()
