from tkinter import *
from PIL import Image, ImageTk
import serial

global blue
blue=False

global red
red=False

global green
green=False

def create_porta():
    global portaUSB
    aux = temp.get()
    portaUSB = serial.Serial(aux, 9600)

def send_command(cod):
    aux = str(cod)
    portaUSB.write(aux.encode())

def comando(op):
    global blue
    global red
    global green
    
    if (op==1 and blue==False):
        print('BLUE LED ON')
        send_command('015')
        texto1 = Label(text='ON', fg='blue')
        texto1.place(x=95,y=65)
        icone = ImageTk.PhotoImage(file='Blue_LED.png')
        botao1.config(image=icone, highlightthickness = 0, bd=0)
        botao1.image = icone
        blue = True

    elif(op==1 and blue==True):
        print('BLUE LED OFF')
        send_command('018')
        texto1 = Label(text='OFF', fg='blue')
        texto1.place(x=95,y=65)
        icone = ImageTk.PhotoImage(file='led.png')
        botao1.config(image=icone, highlightthickness = 0, bd=0)
        botao1.image = icone
        blue = False
        
    elif(op==2 and green==False):
        print('GREEN LED ON')
        send_command('013')
        texto2 = Label(text='ON', fg='green')
        texto2.place(x=235,y=65)
        icone = ImageTk.PhotoImage(file='Green_LED.png')
        botao2.config(image=icone, highlightthickness = 0, bd=0)
        botao2.image = icone
        green = True

    elif(op==2 and green==True):
        print('GREEN LED OFF')
        send_command('016')
        texto2 = Label(text='OFF', fg='green')
        texto2.place(x=235,y=65)
        icone = ImageTk.PhotoImage(file='led.png')
        botao2.config(image=icone, highlightthickness = 0, bd=0)
        botao2.image = icone
        green = False

    elif (op==3 and red==False):
        print('RED LED ON')
        send_command('014')
        texto3 = Label(text='ON', fg='red')
        texto3.place(x=405,y=65)
        icone = ImageTk.PhotoImage(file='Red_LED.png')
        botao3.config(image=icone, highlightthickness = 0, bd=0)
        botao3.image = icone
        red = True

    elif (op==3 and red==True):
        print('RED LED OFF')
        send_command('017')
        texto3 = Label(text='OFF', fg='red')
        texto3.place(x=405,y=65)
        icone = ImageTk.PhotoImage(file='led.png')
        botao3.config(image=icone, highlightthickness = 0, bd=0)
        botao3.image = icone
        red = False


janela = Tk()

janela.title('Arduino Control')

janela.geometry('500x250')

text_Port = Label(text='PORT:').place(x=50,y=200)
temp = StringVar ()
porta = Entry(janela, textvariable = temp).place(x=100,y=200)
botao_port = Button(text='OK', command = create_porta).place(x=250,y=195)

texto1 = Label(text='OFF', fg='blue')
texto1.place(x=95,y=65)
ico1 = ImageTk.PhotoImage(file='led.png')
botao1 = Button(command = lambda: comando(1))
botao1.config(image=ico1, highlightthickness = 0, bd=0)
botao1.place(x=85,y=90)

texto2 = Label(text='OFF', fg='green')
texto2.place(x=235,y=65)
ico2 = ImageTk.PhotoImage(file='led.png')
botao2 = Button(command = lambda: comando(2))
botao2.config(image=ico2, highlightthickness = 0, bd=0)
botao2.place(x=225,y=90)

texto3 = Label(text='OFF', fg='red')
texto3.place(x=405,y=65)
ico3 = ImageTk.PhotoImage(file='led.png')
botao3 = Button(command = lambda: comando(3))
botao3.config(image=ico3, highlightthickness = 0, bd=0)
botao3.place(x=395,y=90)

janela.mainloop()
