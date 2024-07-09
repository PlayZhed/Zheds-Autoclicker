import tkinter as tk 
from pyautogui import click, position, PAUSE, FAILSAFE, FailSafeException
#from pynput.mouse import Listener, Button
#tk.IntVar

'''def print_position():
    while True:
        print(position())'''
#print_position()

#Definitionsbereich für Callback-Funktionen
def uebertragen():
    #der text-Eigenschaft von Label Text zuordnen
    global lb_x_out
    global lb_y_out
    global et_x
    global et_y
    lb_x_out["text"] = (int(et_x.get()))
    lb_y_out["text"] = (int(et_y.get()))

#Fehler abfangen

window = tk.Tk()
window.geometry("1000x1000")
window.title('Autoclicker')

frame = tk.Frame(window)
frame['width'] = 1000
frame['height'] = 1000
frame.place(x = 200,y = 200)


#Funktion Button Klicken (50) für Anzahl der Klicks, Funktion wird x Mal wiederholt
def click_button():
    for i in range (25):
        click(lb_x_out["text"],lb_y_out["text"])
        print('click:', i)   #Zähler für Klicks

PAUSE = 0.0000001 #Soll Zeit in Sekunden zwischen Klicks sein 
FAILSAFE = True


def Ende():
    window.destroy()

'''
lb_clickzahl = tk.Label(window,text='Clickzahl:',fg='black')
lb_clickzahl.grid(row = 1,column = 0,sticky = 'w')
'''



#Position des Mauszeigers anzeigen lassen



#Koordinaten für Mauszeiger
#x = -1513 
#y = 168


#rb_go = tk.Radiobutton(frame,text="Go",value="go"
#rb_go.grid(row = 0,column = 0)

#Überschrift Koordinaten
lb_Eingabe = tk.Label(window,text='Koordinaten:',fg='darkblue')
lb_Eingabe.grid(row = 0,column = 1,sticky = 'we')

#Eingabefelder für Koordinaten
et_x = tk.Entry(window)
et_x.grid(row = 1,column = 1)

et_y = tk.Entry(window)
et_y.grid(row = 2,column = 1)

#Label der 3. Spalte
lb_x_out = tk.Label(window,text=[int(0)],fg='darkblue')
lb_x_out.grid(row = 1,column = 2,sticky = 'we')

lb_y_out = tk.Label(window,text=int(0),fg='blue')
lb_y_out.grid(row = 2,column = 2,sticky = 'we')

#Buttons für Start und Ende
bt_go = tk.Button(window,text='GO',width = 30,fg = 'black',command = lambda:click_button())  #lambda für Verzögerung, erst ausgeführt bei Klick
bt_go.grid(row = 4,column = 1)

bt_Uebertragen = tk.Button(window,text='übertragen',width = 30,fg = 'pink',command = uebertragen)
bt_Uebertragen.grid(row = 5,column = 1)

bt_Ende = tk.Button(window,text='Ende',width = 30,fg = 'black',command = Ende)
bt_Ende.grid(row = 4,column = 2)

window.mainloop()