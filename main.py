from Window import Window
import os 

#clase que inicia el programa
class Init():
    def __init__(self):
        '''from Lexicohtml import Lexicohtml
        from Tokenhtml import Tipo
        a = Lexicohtml(self.__leerArchivo('/home/pedro/Desktop/TestCompi/test.html')) 
        lstoken = a.getListToken()
        print('Fila\tColumna\tLexema\t\t\t\t\t\t\tTipo')
        '''
        ventana = Window()

    def __leerArchivo(self, ruta_archivo):
        with open(ruta_archivo, encoding="utf-8") as f:
                        fileContents = f.read()  # Get all the text from file.
                    # Return text to file contents    
                        return fileContents
        return ""

#el metodo main para inciar el programa
if __name__ == "__main__":
    inciar = Init()
    #pass