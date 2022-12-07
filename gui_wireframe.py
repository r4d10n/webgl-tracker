import PySimpleGUI as sg
import socket
sg.theme("LightBlue")

range_min_x = 1
range_max_x = 100

range_min_y = 1
range_max_y = 100

range_min_z = 1
range_max_z = 100

layout=[
    [sg.Text("Red Ball")],
    [sg.Text("X : "), sg.Slider(orientation ='horizontal', key='redXSlider', range=(range_min_x, range_max_x), enable_events = True),
     sg.Text("Y : "), sg.Slider(orientation ='horizontal', key='redYSlider',range=(range_min_y, range_max_y), enable_events = True),
     sg.Text("Z : "), sg.Slider(orientation ='horizontal', key='redZSlider',range=(range_min_z, range_max_z), enable_events = True)],
    [sg.Text("Green Ball")],
    [sg.Text("X : "), sg.Slider(orientation ='horizontal', key='greenXSlider', range=(range_min_x, range_max_x), enable_events = True),
     sg.Text("Y : "), sg.Slider(orientation ='horizontal', key='greenYSlider',range=(range_min_y, range_max_y), enable_events = True),
     sg.Text("Z : "), sg.Slider(orientation ='horizontal', key='greenZSlider',range=(range_min_z, range_max_z), enable_events = True)],
    [sg.Text("Blue Ball")],
    [sg.Text("X : "), sg.Slider(orientation ='horizontal', key='blueXSlider', range=(range_min_x, range_max_x), enable_events = True),
     sg.Text("Y : "), sg.Slider(orientation ='horizontal', key='blueYSlider',range=(range_min_y, range_max_y), enable_events = True),
     sg.Text("Z : "), sg.Slider(orientation ='horizontal', key='blueZSlider',range=(range_min_z, range_max_z), enable_events = True)],
    ]
window = sg.Window("Positioning",layout)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = 'localhost'
port = 8888
while True:
    event,values=window.read()
    if (event == 'redXSlider') or (event == 'redYSlider') or (event == 'redZSlider'):
        sock.sendto(bytes('{"id":"red", "x":' + str(values['redXSlider']) + ', "y":' + str(values['redYSlider']) + ', "z":' + str(values['redZSlider']) + '}', "utf-8"), (host, port))
    if (event == 'greenXSlider') or (event == 'greenYSlider') or (event == 'greenZSlider'):
        sock.sendto(bytes('{"id":"green", "x":' + str(values['greenXSlider']) + ', "y":' + str(values['greenYSlider']) + ', "z":' + str(values['greenZSlider']) + '}', "utf-8"), (host, port))
    if (event == 'blueXSlider') or (event == 'blueYSlider') or (event == 'blueZSlider'):
        sock.sendto(bytes('{"id":"blue", "x":' + str(values['blueXSlider']) + ', "y":' + str(values['blueYSlider']) + ', "z":' + str(values['blueZSlider']) + '}', "utf-8"), (host, port))
