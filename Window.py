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
        self.root.title("ML WEB EDITOR")
        self.root.resizable(False,False)
        self.root.config(menu=self.menu)
        self.frame.pack()
        self.frame.config(bg="white")
        self.frame.config(width="900", height="600")
        self.initMenu() #metodo que inicia todos los componentes del menu

    #metodo que genera el menu del root window
    def initMenu(self):
        fileMenu = tk.Menu(self.menu, tearoff=0)
        fileMenu.add_command(label="Nuevo", underline=1, command=self.fileDialog)
        fileMenu.add_command(label="Abrir", command=filedialog)
        fileMenu.add_command(label="Guardar")
        fileMenu.add_command(label="Guardar Como")
        fileMenu.add_separator()
        fileMenu.add_command(label="Salir", command=self.root.quit)
        fileEdit = tk.Menu(self.menu,  tearoff=0)
        fileEdit.add_command(label="Copiar")
        fileEdit.add_command(label="Cortar")
        fileEdit.add_command(label="Pegar")
        fileSetting = tk.Menu(self.menu, tearoff=0)
        analiticLex = tk.Menu(self.menu, tearoff=0)
        fileHelp = tk.Menu(self.menu,  tearoff=0)
        fileReport = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=fileMenu)
        self.menu.add_cascade(label="Editar", menu=fileEdit)
        self.menu.add_cascade(label="Analizar", menu=analiticLex)
        self.menu.add_cascade(label="Configuracion", menu=fileSetting)
        self.menu.add_cascade(label="Reporte", menu=fileReport)
        self.menu.add_cascade(label="Ayuda", menu=fileHelp)

    #     
    def save_if_modified(self, event=None):
        if self.editor.edit_modified(): #modified
            response = messagebox.askyesnocancel("Save?", "This document has been modified. Do you want to save changes?") #yes = True, no = False, cancel = None
            if response: #yes/save
                result = self.file_save()
                if result == "saved": #saved
                    return True
                else: #save cancelled
                    return None
            else:
                return response #None = cancel/abort, False = no/discard
        else: #not modified
            return True


    #metodo de la clase para generar el file dialog
    def fileDialog(self, event=None):
        print("file dialg")
        pass



#funcion para abrir archivos    
'''def openFile():
    print("open file")
'''




