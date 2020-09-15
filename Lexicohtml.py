from Tokenhtml import Tipo, Token


class Lexicohtml():
    def __init__(self, text):
        self.listToken = []
        self.outcodehtml = ""
        self.lexerAnalizer(text)

    def lexerAnalizer(self, text):
        self.yycolum = 0
        self.xxrow = 1
        self.lexema = ""
        self.estado = 0
        ls = list(text)
        count = 0
        while count < ls.__len__():
            self.yycolum += 1
            c = ls[count]
            count += 1
            if self.estado == 0:
                if c == '<':
                    self.lexema += c
                    self.outcodehtml += c
                    self.estado = 1
                    continue
                elif c.isalpha():
                    self.lexema += c
                    self.outcodehtml += c
                    self.estado = 8
                    continue
                elif c == '>':
                    self.lexema += c
                    self.outcodehtml += c
                    self.estado = 9
                    count -= 1
                    continue
                elif c == '\"':
                    self.lexema += c
                    self.outcodehtml += c
                    self.estado = 12
                    continue
                elif c == '\'':
                    self.lexema += c
                    self.outcodehtml += c
                    self.estado = 15
                    continue
                elif c == '/':
                    self.estado = 14
                    count -= 1
                    continue
                elif c == '=':
                    self.estado = 14
                    count -= 1
                    continue
                elif c == ' ':
                    self.outcodehtml += c
                    continue
                elif c == '\t':
                    self.outcodehtml += c
                    continue
                elif c == '\r':
                    self.outcodehtml += c
                    continue
                elif c == '\n':
                    self.xxrow += 1
                    self.yycolum = 0
                    continue
                else:
                    pass

            if self.estado == 1:
                if c == '!':
                    self.lexema += c
                    self.outcodehtml += c
                    self.estado = 2
                    continue
                else:
                    self.__addToken(Tipo.MENOR_QUE)
                    count -= 1
                    continue
            if self.estado == 2:
                if c == '-':
                    self.lexema += c
                    self.outcodehtml += c
                    self.estado = 3
                    continue
                else:
                    self.__addToken(Tipo.ERROR)
                    count -= 1
                    continue
            if self.estado == 3:
                if c == '-':
                    self.lexema += c
                    self.outcodehtml += c
                    self.estado = 4
                    continue
                else:
                    self.__addToken(Tipo.ERROR)
                    count -= 1
                    continue
            if self.estado == 4:
                if c == '-':
                    self.lexema += c
                    self.outcodehtml += c
                    self.estado = 5
                    continue
                else:
                    if c == '\n':
                        self.yycolum = 0
                        self.xxrow += 1
                    self.lexema += c
                    self.outcodehtml += c
                    continue
            if self.estado == 5:
                if c == '-':
                    self.lexema += c
                    self.outcodehtml += c
                    self.estado = 6
                    continue
                else:
                    self.estado = 4
                    count -= 1
                    continue
            if self.estado == 6:
                if c == '>':
                    self.lexema += c
                    self.outcodehtml += c
                    self.estado = 7
                    count -= 1
                    continue
                else:
                    self.__addToken(Tipo.ERROR)
                    count -= 1
                    continue
            # estado de aceptacion comentario
            if self.estado == 7:
                if c == '>':
                    self.__addToken(Tipo.COMENTARIO)
                    continue
            # estado para reconocer etiquetas
            if self.estado == 8:
                if c.isalpha():
                    self.lexema += c
                    self.outcodehtml += c
                    continue
                elif c.isdigit():
                    self.lexema += c
                    self.outcodehtml += c
                    continue
                elif self.lexema.lower() == 'html':
                    self.__addToken(Tipo.HTML)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'head':
                    self.__addToken(Tipo.HEAD)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'title':
                    self.__addToken(Tipo.TITLE)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'body':
                    self.__addToken(Tipo.BODY)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'h1':
                    self.__addToken(Tipo.H1)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'h2':
                    self.__addToken(Tipo.H2)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'h3':
                    self.__addToken(Tipo.H3)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'h4':
                    self.__addToken(Tipo.H4)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'h5':
                    self.__addToken(Tipo.H5)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'h6':
                    self.__addToken(Tipo.H6)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'p':
                    self.__addToken(Tipo.P)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'br':
                    self.__addToken(Tipo.BR)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'img':
                    self.__addToken(Tipo.IMG)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'a':
                    self.__addToken(Tipo.A)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'o':
                    self.__addToken(Tipo.O)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'ul':
                    self.__addToken(Tipo.UL)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'li':
                    self.__addToken(Tipo.LI)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'style':
                    self.__addToken(Tipo.STYLE)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'table':
                    self.__addToken(Tipo.TABLE)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'th':
                    self.__addToken(Tipo.TH)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'tr':
                    self.__addToken(Tipo.TR)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'td':
                    self.__addToken(Tipo.TD)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'caption':
                    self.__addToken(Tipo.CAPTION)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'colgroup':
                    self.__addToken(Tipo.COLGROUP)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'col':
                    self.__addToken(Tipo.COL)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'thead':
                    self.__addToken(Tipo.THEAD)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'tbody':
                    self.__addToken(Tipo.TBODY)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'tfoot':
                    self.__addToken(Tipo.TFOOT)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'div':
                    self.__addToken(Tipo.DIV)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'footer':
                    self.__addToken(Tipo.FOOTER)
                    count -= 1
                    continue
                elif c == ' ':
                    self.__addToken(Tipo.ID)
                    count -= 1
                    continue
                elif c == '=':
                    self.__addToken(Tipo.ID)
                    count -= 1
                    continue

            # si es contenido
            if self.estado == 9:
                if c == '>':
                    self.__addToken(Tipo.MAYOR_QUE)
                    if ls.__len__() > count:
                        sigS = ls[count+1]
                        if sigS != '<':
                            self.estado = 10
                            continue
                    continue
            if self.estado == 10:
                if c == '<':
                    self.estado = 11
                    count -= 1
                    continue
                else:
                    if c == '\n':
                        self.yycolum = 0
                        self.xxrow += 1
                    self.lexema += c
                    self.outcodehtml += c
                    continue
            if self.estado == 11:
                if c == '<':
                    self.__addToken(Tipo.CONTENIDO)
                    count -= 1
                    continue

            # reconociendo cadenas
            if self.estado == 12:
                if c == '\"':
                    self.lexema += c
                    self.outcodehtml += c
                    self.estado = 13
                    count -= 1
                    continue
                else:
                    self.lexema += c
                    self.outcodehtml += c
                    continue
            # estado de aceptacion
            if self.estado == 13:
                if c == '\"':
                    self.__addToken(Tipo.CADENA)
                    continue
                elif c == '\'':
                    self.__addToken(Tipo.CADENA)
                    continue

            if self.estado == 15:
                if c == '\'':
                    self.lexema += c
                    self.outcodehtml += c
                    self.estado = 13
                    count -= 1
                    continue
                else:
                    self.lexema += c
                    self.outcodehtml += c
                    continue

            if self.estado == 14:
                if c == '=':
                    self.lexema += c
                    self.outcodehtml += c
                    self.__addToken(Tipo.IGUAL)
                    continue
                elif c == '/':
                    self.lexema += c
                    self.outcodehtml += c
                    self.__addToken(Tipo.DIAGONAL)
                    continue

    # metodo que genera la lista de tokens encontrados

    def __addToken(self, Tipo):
        self.listToken.append(
            Token(Tipo, self.lexema, self.xxrow, self.yycolum))
        self.estado = 0
        self.lexema = ''

    # retorna la lista de tokens

    def getListToken(self):
        return self.listToken

    # retorna el string codigo limpio
    def getSourceClean(self):
        return self.outcodehtml
