
class Lexicojs():
    
    def __init__(self, text):
        self.text = text
        self.lexer_analyzer(self.text)

    def lexer_analyzer(self, text):
        self.yycolum =0
        self.xxrow = 0
        self.lexema = ""
        ls = list(text)
        for c in ls:
            n += 1
            print(n) 
            #self.switch(n)
            
    def switch(self, case):
        switcher={
            0: self.state0()

        }
        return switcher.get(case, "estado Error")

    #validar un palabra de pura letras
    def state0(self):
        print("estado 0\n")

            


        



        