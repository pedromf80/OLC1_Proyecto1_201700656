import tkinter as tk
import tkinter as messagebox
import tkinter as filedialog


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
        self.initMenu() #metodo que inicia todos los componentes del menu
        self.frame.pack()
        self.frame.config(bg="white")
        self.frame.config(width="900", height="600")

    #metodo que genera el menu del root window
    def initMenu(self):
        fileMenu = tk.Menu(self.menu, tearoff=0)
        fileMenu.add_command(label="Nuevo")
        fileMenu.add_command(label="Abrir")
        fileMenu.add_command(label="Guardar")
        fileMenu.add_command(label="Guardar Como")
        fileMenu.add_separator()
        fileMenu.add_command(label="Salir")
        fileEdit = tk.Menu(self.menu,  tearoff=0)
        fileEdit.add_command(label="Copiar")
        fileEdit.add_command(label="Cortar")
        fileEdit.add_command(label="Pegar")
        analiticLex = tk.Menu(self.menu, tearoff=0)
        fileHelp = tk.Menu(self.menu,  tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=fileMenu)
        self.menu.add_cascade(label="Editar", menu=fileEdit)
        self.menu.add_cascade(label="Analizar", menu=analiticLex)
        self.menu.add_cascade(label="Ayuda", menu=fileHelp) 

    def openFile(self):
        print("open file dialog")
        pass
    
    


