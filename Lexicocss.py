
class Lexicocss():
    def __init__(self, text):
        
        self.text = text
        self.lexerAnalizer(text)


    def lexerAnalizer(self, text):
        self.yycolum = 0
        self.xxrow = 1
        self.lexema = ""
        self.estado = 0
        ls = list(text)
        count = 0
        while count < ls.__len__():
            pass
