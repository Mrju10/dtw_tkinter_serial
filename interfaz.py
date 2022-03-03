from tkinter import *
import Printer
import serial_captura_v2
import captura_almacena

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        printerButton = Button(self, text="Graficador", command=self.printerButton)
        CapturaButton = Button(self, text="Comparador", command=self.CapturaButton)
        Almacen16Button = Button(self, text="Grabar movimiento", command=self.Almacen16Button)
        # place button at (0,0)
        exitButton.place(x=0, y=0)
        CapturaButton.place(x=0, y=25)
        printerButton.place(x=0, y=85)
        Almacen16Button.place(x=0, y=55)

    def clickExitButton(self):
        exit()
        
    def printerButton(self):
        print("Graficador") 
        label = Label( root, textvariable= "Graficador", relief=RAISED )
        Printer.func1()
        

    def CapturaButton(self):
        print("Comparador ") 
        label = Label( root, textvariable= "Comparador", relief=RAISED )
        serial_captura_v2.func1()
        

    def Almacen16Button(self):
        print("Grabar caracteres") 
        label = Label( root, textvariable= "Grabar de caracteres", relief=RAISED )
        x=0
        for x in range(15):
            captura_almacena.func1(x)
            x+=1
        

root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")
root.mainloop()