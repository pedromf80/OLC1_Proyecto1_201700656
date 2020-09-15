
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
        auxout = ''
        while count < ls.__len__():
            self.yycolum += 1
            c = ls[count]
            count += 1
            if self.estado == 0:  # caso para la transicion de estados iniciales definidos en el automata
                if c == '/':
                    self.lexema += c
                    auxout += c
                    #self.outcodecss += c
                    self.estado = 1
                    continue
                elif c.isalpha():
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 5
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

                elif c == '#':
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 12
                    continue
                elif c == '-':
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 14
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
                else:
                    self.lexema += c
                    self.__addToken(Tipo.ERROR)
                    continue

            # estado del reconocimiento de comentario multilinea
            if self.estado == 1:
                if c == '*':
                    self.lexema += c
                    auxout += c
                    #self.outcodecss += c
                    auxout += c
                    self.estado = 2
                    continue
                else:
                    self.outcodecss = self.outcodecss + auxout
                    self.__addToken(Tipo.DIAGONAL)
                    continue

            if self.estado == 2:
                if c == '*':
                    self.lexema += c
                    auxout += c
                    #self.outcodecss += c
                    self.estado = 3
                    continue
                else:
                    if c == '\n':
                        self.yycolum = 1
                        self.xxrow += 1
                    if count == ls.__len__():
                        self.__addToken(Tipo.ERROR)
                    self.lexema += c
                    auxout += c
                    #self.outcodecss += c
                    continue

            if self.estado == 3:
                if c == '/':
                    self.lexema += c
                    auxout += c
                    #self.outcodecss += c
                    self.estado = 4
                    count -= 1
                    continue
                else:
                    self.estado = 2
                    count -= 1
                    continue

            if self.estado == 4:
                if c == '/':
                    self.outcodecss = self.outcodecss + auxout
                    auxout = ''
                    self.__addToken(Tipo.COMENTARIO)
                    continue

            # reconociendo ID
            if self.estado == 5:
                if c.isalpha():
                    self.lexema += c
                    self.outcodecss += c
                    continue
                elif c.isdigit():
                    self.lexema += c
                    self.outcodecss += c
                    continue
                elif c == '-':
                    self.lexema += c
                    self.outcodecss += c
                    continue
                elif self.lexema.lower() == 'px':
                    self.__addToken(Tipo.UNIDAD_MEDIDA)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'em':
                    self.__addToken(Tipo.UNIDAD_MEDIDA)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'vh':
                    self.__addToken(Tipo.UNIDAD_MEDIDA)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'vw':
                    self.__addToken(Tipo.UNIDAD_MEDIDA)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'in':
                    self.__addToken(Tipo.UNIDAD_MEDIDA)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'cm':
                    self.__addToken(Tipo.UNIDAD_MEDIDA)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'mm':
                    self.__addToken(Tipo.UNIDAD_MEDIDA)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'pt':
                    self.__addToken(Tipo.UNIDAD_MEDIDA)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'pc':
                    self.__addToken(Tipo.UNIDAD_MEDIDA)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'color':
                    self.__addToken(Tipo.COLOR)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'background-color':
                    self.__addToken(Tipo.BACKGROUND_COLOR)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'background-image':
                    self.__addToken(Tipo.BACKGROUND_IMAGE)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'border':
                    self.__addToken(Tipo.BORDER)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'opacity':
                    self.__addToken(Tipo.OPACITY)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'background':
                    self.__addToken(Tipo.BACKGROUND)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'text-align':
                    self.__addToken(Tipo.TEXT_ALIGN)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'font-family':
                    self.__addToken(Tipo.FONT_FAMILY)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'font-style':
                    self.__addToken(Tipo.FONT_STYLE)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'font-weight':
                    self.__addToken(Tipo.FONT_WEIGHT)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'font-size':
                    self.__addToken(Tipo.FONT_SIZE)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'font':
                    self.__addToken(Tipo.FONT)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'padding-left':
                    self.__addToken(Tipo.PADDING_LEFT)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'padding-right':
                    self.__addToken(Tipo.PADDING_RIGHT)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'padding-bottom':
                    self.__addToken(Tipo.PADDING_BOTTOM)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'padding-top':
                    self.__addToken(Tipo.PADDING_TOP)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'padding':
                    self.__addToken(Tipo.PADDING)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'display':
                    self.__addToken(Tipo.DISPLAY)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'line-height':
                    self.__addToken(Tipo.LINE_HEIGHT)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'width':
                    self.__addToken(Tipo.WIDTH)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'height':
                    self.__addToken(Tipo.HEIGHT)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'margin-top':
                    self.__addToken(Tipo.MARGIN_TOP)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'margin-right':
                    self.__addToken(Tipo.MARGIN_RIGHT)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'margin-bottom':
                    self.__addToken(Tipo.MARGIN_BOTTOM)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'margin-left':
                    self.__addToken(Tipo.MARGIN_LEFT)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'margin':
                    self.__addToken(Tipo.MARGIN)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'border-style':
                    self.__addToken(Tipo.BORDER_STYLE)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'position':
                    self.__addToken(Tipo.POSITION)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'bottom':
                    self.__addToken(Tipo.BOTTOM)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'top':
                    self.__addToken(Tipo.TOP)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'right':
                    self.__addToken(Tipo.RIGHT)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'left':
                    self.__addToken(Tipo.LEFT)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'float':
                    self.__addToken(Tipo.FLOAT)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'clear':
                    self.__addToken(Tipo.CLEAR)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'max-width':
                    self.__addToken(Tipo.MAX_WIDTH)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'min-width':
                    self.__addToken(Tipo.MIN_WIDTH)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'max-height':
                    self.__addToken(Tipo.MAX_HEIGHT)
                    count -= 1
                    continue
                elif self.lexema.lower() == 'min-height':
                    self.__addToken(Tipo.MIN_HEIGHT)
                    count -= 1
                    continue
                else:
                    self.__addToken(Tipo.ID)
                    count -= 1
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
                else:
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
            # estado de aceptacion Digitos con Decimales
            if self.estado == 11:
                if c.isdigit():
                    self.lexema += c
                    self.outcodecss += c
                    continue
                else:
                    self.__addToken(Tipo.NUMERO_FLOAT)
                    count -= 1
                    continue

            # reconocimiento de numeros hexadecimal
            if self.estado == 12:
                if c.isdigit():
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 13
                    continue
                elif self.__HEX(c):
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 13
                    continue
                else:
                    self.__addToken(Tipo.NUMERAL)
                    count -= 1
                    continue

            if self.estado == 13:
                if c.isdigit():
                    self.lexema += c
                    self.outcodecss += c
                    continue
                elif self.__HEX(c):
                    self.lexema += c
                    self.outcodecss += c
                    continue
                else:
                    self.__addToken(Tipo.HEXADECIMAL)
                    count -= 1
                    continue

            if self.estado == 14:
                if c.isalpha():
                    self.lexema += c
                    self.outcodecss += c
                    self.estado = 5
                    continue
                else:
                    self.__addToken(Tipo.GION_MEDIO)
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

    # diccionario de Letras Aceptadas como Hexadecimal
    def __HEX(self, symbol):
        hex = {
            'A': True,
            'B': True,
            'C': True,
            'D': True,
            'E': True,
            'F': True,
        }
        return hex.get(symbol, False)
