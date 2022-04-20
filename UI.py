import PySimpleGUI as sg

layout = [
    [sg.Text("Pass4uBYu", font=("Helvetica", 25))],
    [sg.Text("Keyword: ", font=("Helvetica", 15))],
    [sg.InputText()],
    [sg.Text("Length: ", font=("Helvetica", 15))],
    [sg.InputText()],
    [sg.Button("GENERATE", font=("Helvetica", 15))],
    [sg.Output(size=(40, 20))]
]

# create the window
window = sg.Window("Pass4uBYu", layout, element_justification='c')

# create an event loop
while True:
    event, values = window.read()
    # Press generate button
    if event == "GENERATE":
        continue
    # this should print something here

    # End program of user closes window
    if event == sg.WINDOW_CLOSED:
        break


window.close()
