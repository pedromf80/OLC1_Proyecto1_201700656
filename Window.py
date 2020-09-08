import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from Lexicojs import Lexicojs
from Lexicocss import Lexicocss
from Lexicohtml  import Lexicohtml
from Tokenjs import Tipo
import os

# clase ventana
class Window():
    # constructor de la clase ventana para la app
    def __init__(self):
        self.file_path = None
        self.root = tk.Tk()
        self.frame = tk.Frame()
        self.menu = tk.Menu(self.root)
        self.initComponents()
        self.highlighter(None)
        self.root.mainloop()

    # metodo que inicia todo los componentes de nuestra principal
    def initComponents(self):
        self.root.title("ML WEB EDITOR")
        self.root.resizable(1, 1)
        self.root.config(menu=self.menu)
        self.frame.pack(ipadx=180, expand=1, fill=tk.BOTH)
        self.addTexbox()
        self.addConsole()
        self.initMenu()  # metodo que inicia todos los componentes del menu

    # metodo que genera el menu del root window
    def initMenu(self):
        fileMenu = tk.Menu(self.menu, tearoff=0)
        fileMenu.add_command(label="Nuevo", underline=1,
                             command=self.nuevo_archivo)
        fileMenu.add_command(label="Abrir", command=self.arbrir_archivo)
        fileMenu.add_command(label="Guardar", command=self.guardar_archivo)
        fileMenu.add_command(label="Guardar Como",
                             command=self.guardar_archivo_como)
        fileMenu.add_separator()
        fileMenu.add_command(label="Salir", command=self.file_quit)
        fileEdit = tk.Menu(self.menu,  tearoff=0)
        fileEdit.add_command(label="Adelante", command=self.redo)
        fileEdit.add_command(label="Atras", command=self.undo)
        fileEdit.add_command(label="Limpiar", command=self.reset)
        # fileEdit.add_command(label="Pegar")
        fileSetting = tk.Menu(self.menu, tearoff=0)
        analiticLex = tk.Menu(self.menu, tearoff=0)
        analiticLex.add_command(label='Analizar Archivo',
                                command=self.run_lex_analyzer)
        fileHelp = tk.Menu(self.menu,  tearoff=0)
        fileReport = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=fileMenu)
        self.menu.add_cascade(label="Editar", menu=fileEdit)
        self.menu.add_cascade(label="Analizador Lexico", menu=analiticLex)
        self.menu.add_cascade(label="Configuracion", menu=fileSetting)
        self.menu.add_cascade(label="Reporte", menu=fileReport)
        self.menu.add_cascade(label="Ayuda", menu=fileHelp)

    # genera el texbox del la de entra y salida de texto
    def addTexbox(self):
        self.label = tk.Label(self.frame, text='Entrada', height=1)
        self.label.pack(expand=0, fill=tk.X)
        self.editor = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD)
        self.editor.config(bg='#001a33', insertbackground='white', fg='#b3b3b3')
        self.editor.pack(expand=1, fill=tk.BOTH)
        self.editor.focus()
        self.editor.bind('<Key>', self.highlighter)

    def addConsole(self):
        self.label = tk.Label(self.frame, text='Consola')
        self.label.pack(expand=0, fill=tk.X)
        self.console = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD)
        self.console.configure(height=10, background='black', fg='green')
        self.console.pack(expand=0, fill=tk.BOTH)

    # guardar archivo si se modifico
    def guardar_si_modifico(self, event=None):
        if self.editor.edit_modified():  # modified
            # yes = True, no = False, cancel = None
            resultado = messagebox.askokcancel(
                "Guadar?", "Este documento se modifico! Desea guardar los cambios?")
            if resultado:  # yes/save
                resultado = self.guardar_archivo()
                if resultado == "saved":  # saved
                    return True
                else:  # save cancelled
                    return None
            else:
                return resultado  # None = cancelar/abortar, False = no/descartado
        else:  # no midificado
            return True

    def nuevo_archivo(self, event=None):
        resultado = self.guardar_si_modifico()
        if resultado != None:  # None => Aborted or Save cancelled, False => Discarded, True = Saved or Not modified
            self.editor.delete(1.0, "end")
            self.editor.edit_modified(False)
            self.editor.edit_reset()
            self.file_path = None
        #    self.set_title()

    def arbrir_archivo(self, event=None, ruta_archivo=None):
        try:
            resultado = self.guardar_si_modifico()
            if resultado != None:  # None => Abortar o Guardar cancelar, False =>Descartar, True = Guardar o no modificar
                if ruta_archivo == None:
                    ruta_archivo = filedialog.askopenfilename(initialdir="/home/pedro", title="Select file", filetypes=(
                        ("Archivos html", "*.html"), ("Archivos de estilo css", "*.css"), ("Archivos de fuente js", "*.js"), ("Todos los archivos", "*.*")))
                if ruta_archivo != None and ruta_archivo != "":
                    with open(ruta_archivo, encoding="utf-8") as f:
                        fileContents = f.read()  # Get all the text from file.
                    # Set current text to file contents
                    self.editor.delete(1.0, "end")
                    self.editor.insert(1.0, fileContents)
                    self.editor.edit_modified(False)
                    self.file_path = ruta_archivo
                    self.highlighter(None)
                else:
                    return
        except:
            return

    def guardar_archivo(self, event=None):
        if self.file_path == None:
            resultado = self.guardar_archivo_como()
        else:
            resultado = self.guardar_archivo_como(ruta_archivo=self.file_path)
        return resultado

    def guardar_archivo_como(self, event=None, ruta_archivo=None):
        if ruta_archivo == None:
            ruta_archivo = tk.filedialog.asksaveasfilename(initialdir='/home/pedro', filetypes=(('Archivos html', '*.html'), (
                'Archivos de estilo css', '*.css'), ('Archivos fuente', '*.js'), ('Todos los archivos', '*.*')))  # defaultextension='.txt'
        try:
            with open(ruta_archivo, 'wb') as f:
                text = self.editor.get(1.0, "end-1c")
                f.write(bytes(text, 'UTF-8'))
                self.editor.edit_modified(False)
                self.file_path = ruta_archivo
        #        self.set_title()
                return "saved"
        except FileNotFoundError:
            print('FileNotFoundError')
            return "cancelled"

    def file_quit(self, event=None):
        resultado = self.guardar_si_modifico()
        if resultado != None:  # None => Aborted or Save cancelled, False => Discarded, True = Saved or Not modified
            self.root.destroy()  # sys.exit(0)

    # comandos basicos de ededion de texto
    def undo(self, event=None):
        self.editor.edit_undo()

    def redo(self, event=None):
        self.editor.edit_redo()
        
    def reset(self, event=None):
        self.editor.edit_reset()    

    # metodo para el analisis lexico dependiendo del tipo del archivo
    def run_lex_analyzer(self, event=None):
        if self.file_path == None:
            self.guardar_archivo(None)
        else:    
            input_string = self.editor.get('1.0', 'end-1c')
            x, v = self.file_path.split(".")
            if v == 'js':
                #Lexicojs(input_string)
                self.__jsConsole(input_string)
            if v == 'css':
                Lexicocss(input_string)
            if v == 'html':
                Lexicohtml(input_string)

    def __jsConsole(self, text):
        a = Lexicojs(text)
        lstoken = a.getListToken()
        head = ' Fila\tColumna\t\tTipo\t\t\tLexema\n'
        for token in lstoken:
            if Tipo.ERROR == token.tipoToken:
                head = head+' '+str(token.fila)+'\t'+str(token.columna)+'\t\t'+token.tipoToken.value+'\t\t\t'+token.lexema+'\n'
                #print("Tipo token: "+token.tipoToken.value)
                #print("Lexema: "+token.lexema)
                #print("Columna: "+str(token.columna))
                #print("Fila: "+str(token.fila))
        self.console.delete(1.0, 'end')
        self.console.insert(1.0, head)
        print(a.getSourceClean())
            

    def highlighter(self, event):
        # diccionario de palabras reservadas y color respectivo
        highlightWords = {'if': 'red',
                          'else': 'red',
                          'while': 'red',
                          'true': 'red',
                          'false': 'red',
                          'var': 'red',
                          'find': 'red',
                          'self': 'red',
                          '=' : '#ff751a',
                          'function':'red',
                          'this': 'red'
                          }

        '''the highlight function, called when a Key-press event occurs'''
        for k, v in highlightWords.items():  # iteramos el diccionario
            startIndex = '1.0'
            while True:
                # buscar concurrencia de k
                startIndex = self.editor.search(k, startIndex, tk.END)
                if startIndex:
                    endIndex = self.editor.index('%s+%dc' % (startIndex, (len(k))))  # find end of k
                    self.editor.tag_add(k, startIndex, endIndex)  # add tag to k
                    self.editor.tag_config(k, foreground=v)      # and color it with v
                    startIndex = endIndex  # reset startIndex to continue searching
                else:
                    break

        
