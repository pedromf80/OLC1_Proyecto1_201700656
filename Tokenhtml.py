from enum import Enum

class Tipo(Enum):
    HTML = 'Tag'
    HEAD = 'Tag'
    TITLE = 'Tag'
    BODY = 'Tag'
    H1 = 'Tag'
    H2 = 'Tag'
    H3 = 'Tag'
    H4 = 'Tag'
    H5 = 'Tag'
    H6 = 'Tag'
    P = 'Tag'
    BR = 'Tag'
    IMG = 'Tag'
    A = 'Tag'
    O = 'Tag'
    UL = 'Tag'
    LI = 'Tag'
    STYLE = 'Tag'
    TABLE = 'Tag'
    TH = 'Tag'
    TR = 'Tag'
    TD = 'Tag'
    CAPTION = 'Tag'
    COLGROUP = 'Tag'
    COL = 'Tag'
    THEAD = 'Tag'
    TBODY = 'Tag'
    TFOOT = 'Tag'
    DIV = 'Tag'
    FOOTER = 'Tag'
    ID = 'Id'
    IGUAL = 'Signo Igual' 
    CONTENIDO = 'Contenido'
    MAYOR_QUE = 'Mayor que'
    MENOR_QUE = 'Menor que'
    CADENA = 'Atributo'
    DIAGONAL = 'Diagonal'
    COMENTARIO = 'Comentario'
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
