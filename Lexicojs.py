from Tokenjs import Tipo, Token



class Lexicojs():   
    def __init__(self, text):
        self.listToken = []
        self.lexer_analyzer(text)
               
    def lexer_analyzer(self, text):
        self.yycolum =0
        self.xxrow = 0
        self.lexema = ""
        self.estado=0
        ls = list(text)
        for c in ls:
            self.yycolum +=1
            if self.estado==0: #caso para la transicion de estados
                #print('estado 0')
                if c.isalpha():
                   self.estado =1
                elif c.isdigit():
                    self.estado=2
                elif c =='\"':
                    self.lexema = self.lexema+c
                    self.__addToken(Tipo.DIGITO)
                    self.estado=3
                    break;       
                elif c == '\n':
                    self.xxrow +=1
                    #print('line %s' %(xxrow))
                    #print('column %s' %(yycolum))
                    self.yycolum =0
                   
            elif self.estado ==1:
                #print('estado 1')
                self.estado=0
                

            elif self.estado == 2:
                #print('estado 2')
                self.estado=0        
            
            elif self.estado == 3:
                print('estado 3')
                self.estado=0

    #metodo privado para agregar a la lista los tokens encontrados
    def __addToken(self, Tipo):
        self.listToken.append(Token(Tipo, self.lexema, self.xxrow, self.yycolum))           
        self.estado=0
        self.lexema=''

    #retorna la lista de tokens
    def getListToken(self):
        return self.listToken