from Tokenjs import Tipo, Token


class Lexicojs():
    def __init__(self, text):
        self.listToken = []
        self.outcodejs = ""
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
                    self.outcodejs += c
                    self.estado = 6
                    continue

                elif c.isdigit():
                    self.lexema += c
                    self.outcodejs += c
                    self.estado = 9
                    continue

                elif c == '/':
                    self.lexema += c
                    self.outcodejs += c
                    self.estado = 1
                    continue

                elif c == '\"':
                    self.lexema += c
                    self.outcodejs += c
                    self.estado = 7
                    continue

                elif c == '\'':
                    self.lexema += c
                    self.outcodejs += c
                    self.estado = 13
                    continue

                # recononocimiento de simbolos SB
                elif c == '=':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == '+':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == '-':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == '*':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == '(':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == ')':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == '{':
                    self.estado = 12
                    count -= 1
                    continue
                elif c == '}':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == '[':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == ']':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == ';':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == '.':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == '_':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == ',':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == '>':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == '<':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == ']':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == ']':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == ':':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == '!':
                    self.estado = 12
                    count -= 1
                    continue

                elif c == '\n':
                    self.outcodejs += c
                    self.xxrow += 1
                    self.yycolum = 0
                    continue

                elif c == ' ':
                    self.outcodejs += c
                    continue

                elif c == '\t':
                    self.outcodejs += c
                    continue

                elif c == '\r':
                    self.outcodejs += c
                    continue

                else:
                    self.lexema += c
                    self.__addToken(Tipo.ERROR)
                    continue

            # estado uno del automata reconocimiento de comentarios
            if self.estado == 1:
                if c == '/':
                    self.lexema += c
                    self.outcodejs += c
                    self.estado = 2
                    continue
                elif c == '*':
                    self.lexema += c
                    self.outcodejs += c
                    self.estado = 4
                    continue
                else:
                    self.__addToken(Tipo.DIAGONAL)
                    continue

            if self.estado == 2:
                if c == '\n':
                    self.estado = 3
                    count -= 1
                    continue
                else:
                    self.lexema += c
                    self.outcodejs += c
                    continue

            if self.estado == 3:
                if c == '\n':
                    self.outcodejs += c
                    self.__addToken(Tipo.COMENTARIO_U)
                    self.yycolum = 0
                    self.xxrow += 1
                    continue
                if c == '/':
                    self.__addToken(Tipo.COMENTARIO_M)
                    continue
                else:
                    continue

            if self.estado == 4:
                if c == '*':
                    self.lexema += c
                    self.outcodejs += c
                    self.estado = 5
                    continue
                else:
                    if c == '\n':
                        #self.outcodejs += c
                        self.xxrow += 1
                        self.yycolum = 0
                    self.lexema += c
                    self.outcodejs += c
                    continue

            if self.estado == 5:
                if c == '/':
                    self.lexema += c
                    self.outcodejs += c
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
                    self.outcodejs += c
                    continue
                elif c.isdigit():
                    self.lexema += c
                    self.outcodejs += c
                    continue
                elif c == '_':
                    self.lexema += c
                    self.outcodejs += c
                    continue
                elif self.lexema == 'var':
                    self.__addToken(Tipo.VAR)
                    count -= 1
                    continue
                elif self.lexema == 'if':
                    self.__addToken(Tipo.IF)
                    count -= 1
                    continue
                elif self.lexema == 'else':
                    self.__addToken(Tipo.ELSE)
                    count -= 1
                    continue
                elif self.lexema == 'for':
                    self.__addToken(Tipo.FOR)
                    count -= 1
                    continue
                elif self.lexema == 'while':
                    self.__addToken(Tipo.WHILE)
                    count -= 1
                    continue
                elif self.lexema == 'do':
                    self.__addToken(Tipo.DO)
                    count -= 1
                    continue
                elif self.lexema == 'continue':
                    self.__addToken(Tipo.CONTINUE)
                    count -= 1
                    continue
                elif self.lexema == 'break':
                    self.__addToken(Tipo.BREAK)
                    count -= 1
                    continue
                elif self.lexema == 'return':
                    self.__addToken(Tipo.RETURN)
                    count -= 1
                    continue
                elif self.lexema == 'function':
                    self.__addToken(Tipo.FUNCTION)
                    count -= 1
                    continue
                elif self.lexema == 'constructor':
                    self.__addToken(Tipo.CONSTRUCTOR)
                    count -= 1
                    continue
                elif self.lexema == 'class':
                    self.__addToken(Tipo.CLASS)
                    count -= 1
                    continue
                elif self.lexema == 'new':
                    self.__addToken(Tipo.NEW)
                    count -= 1
                    continue
                elif self.lexema == 'null':
                    self.__addToken(Tipo.NULL)
                    count -= 1
                    continue
                else:
                    self.__addToken(Tipo.ID)
                    count -= 1
                    continue

            # patron para el reconocimiento de cadenas con comillas dobles
            if self.estado == 7:
                if c == '"':
                    self.lexema += c
                    self.outcodejs += c
                    self.estado = 8
                    count -= 1
                    continue
                else:
                    self.lexema += c
                    self.outcodejs += c
                    continue

            # estado de aceptacion de cadenas
            if self.estado == 8:
                self.__addToken(Tipo.CADENA)
                continue

            # estado reconocimiento de digitos enteros y flotantes
            if self.estado == 9:
                if c.isdigit():
                    self.lexema += c
                    self.outcodejs += c
                    continue
                elif c == '.':
                    self.lexema += c
                    self.outcodejs += c
                    self.estado = 10
                    continue
                elif self.__SB(c):
                    self.__addToken(Tipo.DIGITO)
                    count -= 1
                    continue

            # punto donde se empieza a reconocer digitos
            if self.estado == 10:
                if c.isdigit():
                    self.lexema += c
                    self.outcodejs += c
                    self.estado = 11
                    continue
                else:
                    self.__addToken(Tipo.DIGITO)
                    count -=1
                    continue

            if self.estado == 11:
                if c.isdigit():
                    self.lexema += c
                    self.outcodejs += c
                    continue
                elif self.__SB(c):
                    self.__addToken(Tipo.DIGITO)
                    continue

            if self.estado == 13:
                if c == '\'':
                    self.lexema += c
                    self.outcodejs += c
                    self.estado = 8
                    count -= 1
                    continue
                else:
                    self.lexema += c
                    self.outcodejs += c
                    continue

            if self.estado == 12:
                # recononocimiento de simbolos SB
                if c == '=':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.IGUAL)
                    continue

                if c == '+':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.MAS)
                    continue

                if c == '-':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.MENOS)
                    continue

                if c == '*':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.ASTERISCO)
                    continue

                if c == '(':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.PARRENTESIS_IZ)
                    continue

                if c == ')':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.PARRENTESIS_DE)
                    continue

                if c == '{':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.LLAVE_IZ)
                    continue

                if c == '}':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.LLAVE_DE)
                    continue

                if c == '[':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.CORCHETE_IZ)
                    continue

                if c == ']':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.CORCHETE_DE)
                    continue

                if c == ';':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.PUNTO_COMA)
                    continue

                if c == '.':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.PUNTO)
                    continue

                if c == '_':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.GUION_BAJO)
                    continue

                if c == ',':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.COMA)
                    continue

                if c == '>':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.MAYOR_QUE)
                    continue

                if c == '<':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.MENOR_QUE)
                    continue

                if c == ':':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.DOS_PUNTOS)
                    continue

                elif c == ':':
                    self.lexema += c
                    self.outcodejs += c
                    self.__addToken(Tipo.NEGACION)
                    continue

    # diccionario de simbolos aceptados en el lenguaje
    def __SB(self, symbol):
        sb = {
            '.': True,
            '(': True,
            '{': True,
            ',': True,
            ';': True,
            ' ': True,
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

    #retorna el string codigo limpio
    def getSourceClean(self):
        return self.outcodejs    
