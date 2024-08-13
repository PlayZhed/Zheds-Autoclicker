import tkinter as tk
import time
from pynput import mouse, keyboard
from pyautogui import click, position, PAUSE, FAILSAFE, FailSafeException
from pynput.mouse import Listener, Button


##### bei 0 - unendlich viele Klicks

def click_button():
    for i in range (lb_amount_out["text"]):
        x = int(lb_x_out["text"])
        y = int(lb_y_out["text"])
        click(x,y)
        print('click:', i)

PAUSE = 0.0000001 #Soll Zeit in Sekunden zwischen Klicks sein 
FAILSAFE = True

def Ende():
    window.destroy()

#Definitionsbereich für Callback-Funktionen
def uebertragen():
    #der text-Eigenschaft von Label Text zuordnen - global damit es für alle gilt
    global lb_x_out
    global lb_y_out
    global lb_amount_out
    lb_x_out["text"] = int(et_x.get())
    lb_y_out["text"] = int(et_y.get())
    lb_amount_out["text"] =int(et_amount.get())
    
#
#Fehler abfangen, wenn str statt int eingegeben wird
#


pressed_location = 0, 0

freigabe = False

def on_click(x, y ,button, pressed):
    if freigabe == True:
        global pressed_location
    if pressed and button == Button.left:
        pressed_location = x, y
        et_x.delete(0, tk.END)  #löscht die Eingabe
        et_x.insert(0, str(x))  #gibt die Koordinate ein
        et_y.delete(0, tk.END)  
        et_y.insert(0, str(y))  
        print(f'x={x} and y={y}')
        if pressed:    #stopt den Listener
            return False

def get_coordinates():
    with mouse.Listener(on_click=on_click) as listener:

        tk.mainloop()

        listener.join()
    

#Start GUI

window = tk.Tk()
window.geometry("1000x500")
window.title('Clickbot')

frame = tk.Frame(window)
frame['width'] = 100
frame['height'] = 100
frame.place(x = 200,y = 200)


#Position des Mauszeigers anzeigen lassen


#Überschrift Koordinaten
lb_Eingabe = tk.Label(window,text='Koordinaten:',fg='darkblue')
lb_Eingabe.grid(row = 0,column = 1,sticky = 'we')

#Überschrift Klickzahl
lb_Eingabe = tk.Label(window,text='Klickzahl:',fg='darkblue')
lb_Eingabe.grid(row = 6,column = 1,sticky = 'we')

#Eingabefelder für Koordinaten
et_x = tk.Entry(window)
et_x.grid(row = 1,column = 1)

et_y = tk.Entry(window)
et_y.grid(row = 2,column = 1)

#Eingabefeld für Klickzahl
et_amount = tk.Entry(window)
et_amount.grid(row = 7, column = 1)

#Anzeige für übertragene Werte
lb_x_out = tk.Label(window,text=[int(0)],fg='darkblue')
lb_x_out.grid(row = 1,column = 2,sticky = 'we')

lb_y_out = tk.Label(window,text=[int(0)],fg='blue')
lb_y_out.grid(row = 2,column = 2,sticky = 'we')

#Ausgabe Klickzahl
lb_amount_out = tk.Label(window,text=[int(0)],fg='black')
lb_amount_out.grid(row = 7, column = 2,sticky = 'n')

#Buttons für Start und Ende
bt_go = tk.Button(window,text='GO',width = 30,fg = 'black',command = lambda:click_button())  #lambda für Verzögerung, erst ausgeführt bei Klick
bt_go.grid(row = 4,column = 1)

bt_Uebertragen = tk.Button(window,text='übertragen',width = 30,fg = 'black',command = uebertragen)
bt_Uebertragen.grid(row = 5,column = 1)

bt_Ende = tk.Button(window,text='Ende',width = 30,fg = 'black',command = Ende)
bt_Ende.grid(row = 4,column = 2)

bt_on_click = tk.Button(window,text='Koordinaten per Klick',width = 30,fg = 'black',command = get_coordinates)
bt_on_click.grid(row = 5,column = 2)

window.mainloop()