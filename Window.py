import tkinter as tk
import tkinter as messagebox
import tkinter as filedialog
from tkinter import  scrolledtext


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
        self.root.resizable(1,1)
        self.root.config(menu=self.menu)
        self.frame.pack()
        self.frame.config(bg="white")
        self.frame.config(width="900", height="600")
        self.addTexbox()
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

    #genera el texbox del la de entra y salida de texto
    def addTexbox(self):
        self.yscrollbar = tk.Scrollbar(self.frame, orient="vertical")
        self.editor = tk.Text(self.frame, yscrollcommand=self.yscrollbar.set)
        self.editor.pack(side="left", fill="both", expand=1)
        self.editor.config( wrap = "word", # use word wrapping
               undo = True, # Tk 8.4 
               width = 80 )        
        self.editor.focus()
        self.yscrollbar.pack(side="right", fill="y")
        self.yscrollbar.config(command=self.editor.yview)        
        self.frame.pack(fill="both", expand=1)





    '''
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
    
    def file_new(self, event=None):
        result = self.save_if_modified()
        if result != None: #None => Aborted or Save cancelled, False => Discarded, True = Saved or Not modified
            self.editor.delete(1.0, "end")
            self.editor.edit_modified(False)
            self.editor.edit_reset()
            self.file_path = None
            self.set_title()
            

    def file_open(self, event=None, filepath=None):
        result = self.save_if_modified()
        if result != None: #None => Aborted or Save cancelled, False => Discarded, True = Saved or Not modified
            if filepath == None:
                filepath = filedialog.askopenfilename()
            if filepath != None  and filepath != '':
                with open(filepath, encoding="utf-8") as f:
                    fileContents = f.read()# Get all the text from file.           
                # Set current text to file contents
                self.editor.delete(1.0, "end")
                self.editor.insert(1.0, fileContents)
                self.editor.edit_modified(False)
                self.file_path = filepath

    def file_save(self, event=None):
        if self.file_path == None:
            result = self.file_save_as()
        else:
            result = self.file_save_as(filepath=self.file_path)
        return result

    def file_save_as(self, event=None, filepath=None):
        if filepath == None:
            filepath = filedialog.asksaveasfilename(filetypes=(('Text files', '*.txt'), ('Python files', '*.py *.pyw'), ('All files', '*.*'))) #defaultextension='.txt'
        try:
            with open(filepath, 'wb') as f:
                text = self.editor.get(1.0, "end-1c")
                f.write(bytes(text, 'UTF-8'))
                self.editor.edit_modified(False)
                self.file_path = filepath
                self.set_title()
                return "saved"
        except FileNotFoundError:
            print('FileNotFoundError')
            return "cancelled"

    def file_quit(self, event=None):
        result = self.save_if_modified()
        if result != None: #None => Aborted or Save cancelled, False => Discarded, True = Saved or Not modified
            self.root.destroy() #sys.exit(0)

    def set_title(self, event=None):
        if self.file_path != None:
            title = os.path.basename(self.file_path)
        else:
            title = "Untitled"
        self.root.title(title + " - " + self.TITLE)
        
    def undo(self, event=None):
        self.editor.edit_undo()
        
    def redo(self, event=None):
        self.editor.edit_redo()     
    '''


    #metodo de la clase para generar el file dialog
    def fileDialog(self, event=None):
        print("file dialg")
        pass



#funcion para abrir archivos    
'''def openFile():
    print("open file")
'''




