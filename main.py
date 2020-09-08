from Window import Window
import os 

#clase que inicia el programa
class Init():
    def __init__(self):
        from Lexicojs import Lexicojs
        a = Lexicojs(self.readF())
        lstoken = a.getListToken()
        for token in lstoken:
           #pass
            print("Tipo token: "+token.tipoToken.value)
            print("Lexema: "+token.lexema)
            print("Columna: "+str(token.columna))
            print("Fila: "+str(token.fila))
           #print('\n')
        #pass 
        #ventana = Window()

    def readF(self):
        with open('/home/pedro/Desktop/TestCompi/ejemplo.js') as f:
             filecontent = f.read()
        return filecontent    
        
#el metodo main para inciar el programa
if __name__ == "__main__":
    inciar = Init()
    #pass