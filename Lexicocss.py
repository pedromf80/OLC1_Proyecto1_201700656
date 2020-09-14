
from Tokencss import Tipo, Token


class Lexicocss():
    def __init__(self, text):
        self.listToken = []
        self.outcodecss = ""
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
            if self.estado == 0:  # caso para la transicion de estados iniciales definidos en el automata
                if c == '/':
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 1
                    continue
                elif c == '\"':
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 6
                    continue

                elif c == '{':
                    self.estado = 8
                    count -= 1
                    continue

                elif c == '}':
                    self.estado = 8
                    count -= 1
                    continue

                elif c == '(':
                    self.estado = 8
                    count -= 1
                    continue

                elif c == ')':
                    self.estado = 8
                    count -= 1
                    continue

                elif c == '*':
                    self.estado = 8
                    count -= 1
                    continue

                elif c == '+':
                    self.estado = 8
                    count -= 1
                    continue

                elif c == ':':
                    self.estado = 8
                    count -= 1
                    continue

                elif c == ',':
                    self.estado = 8
                    count -= 1
                    continue

                elif c == ';':
                    self.estado = 8
                    count -= 1
                    continue

                elif c == '.':
                    self.estado = 8
                    count -= 1
                    continue

                elif c == '%':
                    self.estado = 8
                    count -= 1
                    continue

                elif c.isdigit():
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 9
                    continue

                elif c == ' ':
                    self.outcodecss += c
                    continue

                elif c == '\t':
                    self.outcodecss += c
                    continue

                elif c == '\r':
                    self.outcodecss += c
                    continue
                elif c == '\n':
                    self.outcodecss += c
                    self.yycolum = 0
                    self.xxrow += 1
                    continue
                '''else:
                    self.lexema += c
                    self.__addToken(Tipo.ERROR)
                    continue '''

            # estado del reconocimiento de comentario multilinea
            if self.estado == 1:
                if c == '*':
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 2
                    continue
                else:
                    self.__addToken(Tipo.DIAGONAL)
                    continue

            if self.estado == 2:
                if c == '*':
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 3
                    continue
                else:
                    if c == '\n':
                        self.yycolum = 1
                        self.xxrow += 1
                    if count == ls.__len__():
                        self.__addToken(Tipo.ERROR)
                    self.lexema += c
                    self.outcodecss += c
                    continue

            if self.estado == 3:
                if c == '/':
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 4
                    count -= 1
                    continue
                else:
                    self.estado = 2
                    count -= 1
                    continue

            if self.estado == 4:
                if c == '/':
                    self.__addToken(Tipo.COMENTARIO)
                    continue

            # reconocimiento de cadena
            if self.estado == 6:
                if c == '\"':
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 7
                    count -= 1
                    continue
                else:
                    if count == ls.__len__():
                        self.__addToken(Tipo.ERROR)
                    self.lexema += c
                    self.outcodecss += c
                    continue

            # estado de Aceptacion
            if self.estado == 7:
                if c == '\"':
                    self.__addToken(Tipo.CADENA)
                    continue

            # Estado de aceptacion Simbolos
            if self.estado == 8:
                if c == '{':
                    self.lexema += c
                    self.outcodecss += c
                    self.__addToken(Tipo.LLAVE_IZ)
                    continue

                elif c == '}':
                    self.lexema += c
                    self.outcodecss += c
                    self.__addToken(Tipo.LLAVE_DE)
                    continue

                elif c == '(':
                    self.lexema += c
                    self.outcodecss += c
                    self.__addToken(Tipo.PARENTESIS_I)
                    continue

                elif c == ')':
                    self.lexema += c
                    self.outcodecss += c
                    self.__addToken(Tipo.PARENTESIS_D)
                    continue

                elif c == '*':
                    self.lexema += c
                    self.outcodecss += c
                    self.__addToken(Tipo.ASTERISCO)
                    continue

                elif c == '+':
                    self.lexema += c
                    self.outcodecss += c
                    self.__addToken(Tipo.MAS)
                    continue

                elif c == ':':
                    self.lexema += c
                    self.outcodecss += c
                    self.__addToken(Tipo.DOS_PUNTOS)
                    continue

                elif c == ',':
                    self.lexema += c
                    self.outcodecss += c
                    self.__addToken(Tipo.COMA)
                    continue

                elif c == ';':
                    self.lexema += c
                    self.outcodecss += c
                    self.__addToken(Tipo.PUNTO_COMA)
                    continue

                elif c == '.':
                    self.lexema += c
                    self.outcodecss += c
                    self.__addToken(Tipo.PUNTO)
                    continue

                elif c == '%':
                    self.lexema += c
                    self.outcodecss += c
                    self.__addToken(Tipo.PORCENTAJE)
                    continue

            # reconocimiento de numeros
            if self.estado == 9:
                if c.isdigit():
                    self.lexema += c
                    self.outcodecss += c
                    continue
                elif c == '.':
                    self.lexema += c
                    self. outcodecss += c
                    self.estado = 10
                    continue
                elif self.__SB(c):
                    self.yycolum -= 1
                    self.__addToken(Tipo.DIGITO)
                    count -= 1
                    continue

            if self.estado == 10:
                if c.isdigit():
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 11
                    continue
                else:
                    self.lexema = self.lexema.replace('.', '')
                    self.__addToken(Tipo.DIGITO)
                    count -= 2
                    continue

            if self.estado == 11:
                if c.isdigit():
                    self.lexema += c
                    self.outcodecss += c
                    continue
                else:
                    self.__addToken(Tipo.NUMERO_FLOAT)
                    count -= 1
                    continue

    # metodo privado para agregar a la lista los tokens encontrados

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
        return self.outcodecss

     # diccionario de simbolos aceptados en el lenguaje
    def __SB(self, symbol):
        sb = {
            '(': True,
            '{': True,
            ')': True,
            '}': True,
            ',': True,
            ':': True,
            ';': True,
            ' ': True,
            '\n': True,
            '%': True,
            '.': True,
        }
        return sb.get(symbol, False)
