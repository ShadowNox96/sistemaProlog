from tkinter import ttk
from tkinter import *
from app import *
from speech import *
from speak import *

class Inicio:

    def __init__(self, window):
        self.wind =window
        self.wind.title('Consulta Prolog')

        # Creacion del frame 
        frame = LabelFrame(self.wind, text = 'Realiza una pregunta')
        frame.grid(row = 0, column =0, columnspan = 3, pady = 20, sticky = W + E)

        #Label 
        Label(frame, text = 'Pregunta: ').grid(row = 2, column = 0)
        self.pregunta = Entry(frame)
        self.pregunta.grid(row = 2, column = 1)
        self.pregunta.focus()

        #Button
        ttk.Button(frame, text = 'Consultar', command = self.consultar).grid(row = 4, column = 0)
        ttk.Button(frame, text = 'Hablar', command = self.speech).grid(row = 4, column = 1)


        #Output Message
        self.message1 = Label(text = '', fg = 'black')
        self.message1.grid(row = 5, column = 0, columnspan = 2)
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 6, column = 0, columnspan = 2, sticky = W + E) 
        self.messageSpeech = Label(text = '', fg = 'black')
        self.messageSpeech.grid(row = 3, column = 0, columnspan =2)
        self.returnSpeech = Label(text = '', fg = 'green')
        self.returnSpeech.grid(row = 4, column = 0, columnspan = 2)

    def consultar(self):
        value = consultaProlog(self.pregunta.get())
        self.message1['text'] = 'RESPUESTA: '
        self.message['text'] = '{}'.format(value)
        self.pregunta.delete(0, END)
        reproducirTexto(value)

    def speech(self):
        self.pregunta.delete(0, END)
        value = main()
        self.messageSpeech['text'] = 'Usted dijo?'
        self.returnSpeech['text'] = '{}'.format(value) 
        self.pregunta.insert(0, str.lower(value))

if __name__ == '__main__':
    window = Tk()
    application = Inicio(window)
    window.mainloop()