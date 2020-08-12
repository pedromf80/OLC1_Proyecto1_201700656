import tkinter as tk

#clase ventana
class Window():
    #constructor de la clase ventana para la app
    def __init__(self):
        self.root = tk.Tk()
        self.frame = tk.Frame()
        self.menu = tk.Menu(self.root)
        self.initComponents()
        self.root.mainloop()

    #metodo que inicia todo los componentes de nuestra principal
    def initComponents(self):
        self.root.title("Ventana Principal")
        self.root.resizable(False,False)
        self.root.config(menu=self.menu)
        self.frame.pack()
        self.frame.config(bg="white")
        self.frame.config(width="900", height="600")

    #metodo que genera el menu del programa
    def initMenu(self):
        
        pass    
        
       

    
    


