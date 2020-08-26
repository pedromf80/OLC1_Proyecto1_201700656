from Window import Window
import os 

#clase que inicia el programa
class Init():
    def __init__(self):
        from Lexicojs import Lexicojs
        a = Lexicojs(self.readF())
        lstoken = a.getListToken()
        for token in lstoken:
            print(token.tipoToken.value)
            print(token.lexema)
            print(token.columna)
            print(token.fila)
        #pass
        #ventana = Window()

    def readF(self):
        with open('/home/pedro/Desktop/TestCompi/fuente.js') as f:
             filecontent = f.read()
        return filecontent    

       
        
#el metodo main para inciar el programa
if __name__ == "__main__":
    inciar = Init()
    #pass