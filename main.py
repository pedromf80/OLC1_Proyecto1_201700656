from Window import Window
import os 

#clase que inicia el programa
class Init():
    def __init__(self):
        from Lexicojs import Lexicojs
        Lexicojs(self.readF())
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