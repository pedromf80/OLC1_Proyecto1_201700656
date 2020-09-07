from Tokenjs import Tipo, Token


class Lexicojs():
    def __init__(self, text):
        self.listToken = []
        self.lexer_analyzer(text)

    def lexer_analyzer(self, text):
        self.yycolum = 0
        self.xxrow = 1
        self.lexema = ""
        self.estado = 0
        ls = list(text)
        count = 0
        while (count < ls.__len__()):
            self.yycolum += 1
            c = ls[count]
            count += 1
            if self.estado == 0:  # caso para la transicion de estados
                if c.isalpha():
                    self.lexema +=c
                    self.estado = 6

                   #self.estado =10
                if c.isdigit(): #caso para la transicion con Digito
                    pass
                    '''self.estado = 10
                    count -= 1
                    '''
                if c == '/':
                    self.lexema += c
                    self.estado = 1
                    continue
                if c == '\"':
                    pass
                    #self.lexema = self.lexema+c
                    # self.__addToken(Tipo.DIGITO)
                   # self.estado=3

                if c == '\n':
                    self.xxrow += 1
                    self.yycolum = 0
                    continue

            # estado uno del automata reconocimiento de comentarios
            if self.estado == 1:
                if c == '/':
                    self.lexema += c
                    self.estado = 2
                    continue
                elif c == '*':
                    self.lexema += c
                    self.estado = 4
                    continue
                else: 
                    self.__addToken(Tipo.ERROR)
                    continue

            if self.estado == 2:
                if c == '\n':
                    self.estado = 3
                    count -= 1
                    continue
                else:
                    self.lexema += c

            if self.estado == 3:

                if c == '\n':
                    self.__addToken(Tipo.COMENTARIO_U)
                    self.yycolum = 0
                    self.xxrow += 1
                    continue
                if c == '/':
                    self.__addToken(Tipo.COMENTARIO_M)
                    continue

            if self.estado == 4:
                if c == '*':
                    self.lexema += c
                    self.estado = 5
                    continue
                else:
                    if c == '\n':
                        self.xxrow += 1
                    self.lexema += c

            if self.estado == 5:
                if c == '/':
                    self.lexema += c
                    self.estado = 3
                    count -= 1
                    continue
                else:
                    self.estado = 4
                    count -= 1
                    continue

            # punto donde se empieza a reconocer digitos
            if self.estado == 10:
                if c.isdigit():
                    self.lexema += c
                elif c == '.':
                    self.lexema += c
                    self.estado = 11
                elif c == ' ' or c == ';':
                    count -= 1
                    self.__addToken(Tipo.DIGITO)

            if self.estado == 11:
                if c.isdigit():
                    self.lexema += c
                elif c == ' ':
                    self.__addToken(Tipo.DIGITO)
            if self.estado == 13:
                pass

    # metodo privado para agregar a la lista los tokens encontrados

    def __addToken(self, Tipo):
        self.listToken.append(
            Token(Tipo, self.lexema, self.xxrow, self.yycolum))
        self.estado = 0
        self.lexema = ''

    # retorna la lista de tokens
    def getListToken(self):
        return self.listToken
