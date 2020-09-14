from enum import Enum


class Tipo(Enum):
    COLOR = 'Palabra Reservada'
    BACKGROUND_COLOR = 'Palabra Reservada'
    BACKGROUND_IMAGE = 'Palabra Reservada'
    BORDER = 'Palabra Reservada'
    OPACITY = 'Palabra Reservada'
    BACKGROUND = 'Palabra Reservada'
    TEXT_ALIGN = 'Palabra Reservada'
    FONT_FAMILY = 'Palabra Reservada'
    FONT_STYLE = 'Palabra Reservada'
    FONT_WEIGHT = 'Palabra Reservada'
    FONT_SIZE = 'Palabra Reservada'
    FONT = 'Palabra Reservada'
    PADDING_LEFT = 'Palabra Reservada'
    PADDING_RIGHT = 'Palabra Reservada'
    PADDING_BOTTOM = 'Palabra Reservada'
    PADDING_TOP = 'Palabra Reservada'
    PADDING = 'Palabra Reservada'
    DISPLAY = 'Palabra Reservada'
    LINE_HEIGHT = 'Palabra Reservada'
    WIDTH = 'Palabra Reservada'
    HEIGHT = 'Palabra Reservada'
    MARGIN_TOP = 'Palabra Reservada'
    MARGIN_RIGHT = 'Palabra Reservada'
    MARGIN_BOTTOM = 'Palabra Reservada'
    MARGIN_LEFT = 'Palabra Reservada'
    MARGIN = 'Palabra Reservada'
    BORDER_STYLE = 'Palabra Reservada'
    POSITION = 'Palabra Reservada'
    BOTTOM = 'Palabra Reservada'
    TOP = 'Palabra Reservada'
    RIGHT = 'Palabra Reservada'
    LEFT = 'Palabra Reservada'
    FLOAT = 'Palabra Reservada'
    CLEAR = 'Palabra Reservada'
    MAX_WIDTH = 'Palabra Reservada'
    MIN_WIDTH = 'Palabra Reservada'
    MAX_HEIGHT = 'Palabra Reservada'
    MIN_HEIGHT = 'Palabra Reservada'
    LLAVE_IZ = 'LLave Izquierdo'
    LLAVE_DE = 'Llave Derecho'
    DIGITO = 'Digito'
    COMA = 'Coma'
    PUNTO = 'Punto'
    COMENTARIO = 'Comentario'
    PUNTO_COMA = 'Punto y coma'
    DOS_PUNTOS = "Dos Puntos"
    PARENTESIS_I = "Parentesis Izquierdo"
    PARENTESIS_D = "Parentisis Derecho"
    CADENA = 'Cadena'
    MENOS = 'Signo Menos'
    PORCENTAJE = 'Porcentaje'
    MAS = 'Mas'
    DIAGONAL = 'Diagonal'
    ASTERISCO = 'Asterisco'
    NUMERAL = 'Numeral'
    HEXADECIMAL = 'Digito Hexadecimal'
    NUMERO_FLOAT = 'Digito Decimal'
    VALOR = 'Valor'
    UNIDAD_MEDIDA = 'Unidad de medida'
    ERROR = 'Error Lexico'
    
class Token():
    def __init__(self, tipo, lexema, fila, columna):
        self.tipoToken = tipo
        self.lexema = lexema
        self.fila = fila
        self.columna = columna

    def getTipo(self):
        return self.tipoToken

    def getLexema(self):
        return self.lexema

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna
