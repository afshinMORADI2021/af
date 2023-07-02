import PySimpleGUI as sg


label1 = sg.Text("select")

input1 = sg.Input()

choose_button1 = sg.FileBrowse("choose")

label2 = sg.Text("select detination")

input2 = sg.Input()

choose_button2 = sg.FolderBrowse("choose")

compress_button = sg.Button("compress")
window = sg.Window("file comprssor",
                     layout =[[label1, input1, choose_button1],
                             [label2, input2, choose_button2],
                                [compress_button]])
window.read()
window.close()