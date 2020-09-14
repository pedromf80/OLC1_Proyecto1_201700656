from Window import Window
import os 

#clase que inicia el programa
class Init():
    def __init__(self):
        from Lexicocss import Lexicocss
        a = Lexicocss(self.__leerArchivo('/home/pedro/Desktop/TestCompi/ejemplo.css')) 
        lstoken = a.getListToken()
        print('Columa\tFila\tLexema\t\t\t\t\t\t\tTipo')
        for token in lstoken:
            print(''+str(token.columna)+'\t'+str(token.fila)+'\t'+token.lexema+'\t\t\t\t\t\t\t'+token.tipoToken.value)
            #print(a.getSourceClean())
        #ventana = Window()

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