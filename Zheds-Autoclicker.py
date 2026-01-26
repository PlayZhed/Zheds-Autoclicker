import tkinter as tk
import time
import threading
import pyautogui
from pynput import mouse
from pynput import keyboard as pynput_keyboard
from pyautogui import click, position, PAUSE, FAILSAFE, FailSafeException
from pynput.mouse import Listener, Button

stop_clicking = False

pyautogui.PAUSE = 0.0001

def click_button():
    global stop_clicking
    x = int(lb_x_out["text"])
    y = int(lb_y_out["text"])
    clicks = int(lb_amount_out["text"]) or 25

    def click_loop():
        global stop_clicking
        stop_clicking = False
        count = 0
        while count < clicks and not stop_clicking:
            pyautogui.moveTo(x, y)
            pyautogui.click()
            print('click:', count)
            count += 1
            time.sleep(0.001)
        print("done or stopped!")

    threading.Thread(target=click_loop, daemon=True).start()


def esc_listener():
    def on_press(key):
        global stop_clicking
        if key == pynput_keyboard.Key.esc:
            stop_clicking = True
            return False
    listener = pynput_keyboard.Listener(on_press=on_press)
    listener.start()

PAUSE = 0.0000001
FAILSAFE = True

def Exit():
    window.destroy()


def transfer():
    try:
        lb_x_out["text"] = et_x.get() or "0"
        lb_y_out["text"] = et_y.get() or "0"
        lb_amount_out["text"] = et_amount.get() or "25"
    except ValueError:
        print("only numbers")


pressed_location = 0, 0

release = False

def on_click(x, y ,button, pressed):
    if release == True:
        global pressed_location
    if pressed and button == Button.left:
        pressed_location = x, y
        et_x.delete(0, tk.END)
        et_x.insert(0, str(x))
        et_y.delete(0, tk.END)
        et_y.insert(0, str(y))
        print(f'x={x} and y={y}')
        if pressed:    #stopt den Listener
            return False

def get_coordinates():
    with mouse.Listener(on_click=on_click) as listener:

        tk.mainloop()

        listener.join()


window = tk.Tk()
window.geometry("1000x500")
window.title('Autoclicker')

frame = tk.Frame(window)
frame['width'] = 100
frame['height'] = 100
frame.place(x = 200,y = 200)



lb_Input = tk.Label(window,text='coordinates:',fg='darkblue')
lb_Input.grid(row = 0,column = 1,sticky = 'we')

lb_Input = tk.Label(window,text='how many clicks:',fg='darkblue')
lb_Input.grid(row = 6,column = 1,sticky = 'we')

#entry coordinates
et_x = tk.Entry(window)
et_x.grid(row = 1,column = 1)

et_y = tk.Entry(window)
et_y.grid(row = 2,column = 1)

#entry how many clicks
et_amount = tk.Entry(window)
et_amount.grid(row = 7, column = 1)

#transfered values
lb_x_out = tk.Label(window,text="0",fg='darkblue')
lb_x_out.grid(row = 1,column = 2,sticky = 'we')

lb_y_out = tk.Label(window,text="0",fg='blue')
lb_y_out.grid(row = 2,column = 2,sticky = 'we')

#output number of clicks
lb_amount_out = tk.Label(window,text="0",fg='black')
lb_amount_out.grid(row = 7, column = 2,sticky = 'n')

#buttons start and end
bt_start = tk.Button(window,text='start clicking',width = 30,fg = 'black',command = click_button)
bt_start.grid(row = 4,column = 1)

bt_Transfer = tk.Button(window,text='transfer',width = 30,fg = 'black',command = transfer)
bt_Transfer.grid(row = 5,column = 1)

bt_Exit = tk.Button(window,text='exit',width = 30,fg = 'black',command = Exit)
bt_Exit.grid(row = 4,column = 2)

bt_on_click = tk.Button(window,text='coordinates per click',width = 30,fg = 'black',command = get_coordinates)
bt_on_click.grid(row = 5,column = 2)

def start_esc_listener():
    esc_listener()

threading.Thread(target=start_esc_listener, daemon=True).start()

window.mainloop()