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
                    self.lexema += c
                    self.estado = 6
                    continue
                   #self.estado =10
                if c.isdigit():
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
                        self.yycolum = 0
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

            # reconocimiento de palabras reservadas e ID's
            if self.estado == 6:
                if c.isalpha():
                    self.lexema += c
                elif c.isdigit():
                    self.lexema += c
                elif c == '_':
                    self.lexema += c
                elif self.lexema == 'var':
                    self.__addToken(Tipo.VAR)
                    continue
                elif self.lexema == 'if':
                    self.__addToken(Tipo.IF)
                    continue
                elif self.lexema == 'else':
                    self.__addToken(Tipo.ELSE)
                    continue
                elif self.lexema == 'for':
                    self.__addToken(Tipo.FOR)
                    continue
                elif self.lexema == 'while':
                    self.__addToken(Tipo.WHILE)
                    continue
                elif self.lexema == 'do':
                    self.__addToken(Tipo.DO)
                    continue
                elif self.lexema == 'continue':
                    self.__addToken(Tipo.CONTINUE)
                    continue
                elif self.lexema == 'break':
                    self.__addToken(Tipo.BREAK)
                    continue
                elif self.lexema == 'return':
                    self.__addToken(Tipo.RETURN)
                    continue
                elif self.lexema == 'function':
                    self.__addToken(Tipo.FUNCTION)
                    continue
                elif self.lexema == 'constructor':
                    self.__addToken(Tipo.CONSTRUCTOR)
                    continue
                elif self.lexema == 'class':
                    self.__addToken(Tipo.CLASS)
                    continue
                elif self.lexema == 'new':
                    self.__addToken(Tipo.NEW)
                    continue
                else:
                    self.__addToken(Tipo.ID)
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

    # diccionario de simbolos aceptados en el lenguaje
    def __SB(self, symbol):
        sb = {
            '.': True,
            '(': True,
            '{': True,
        }
        return sb.get(symbol, False)

    # metodo privado para agregar a la lista los tokens encontrados

    def __addToken(self, Tipo):
        self.listToken.append(
            Token(Tipo, self.lexema, self.xxrow, self.yycolum))
        self.estado = 0
        self.lexema = ''

    # retorna la lista de tokens
    def getListToken(self):
        return self.listToken
