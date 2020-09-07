
from enum import Enum

class Tipo(Enum):
    COMENTARIO_U = 'Comentario Unilinea'
    COMENTARIO_M = 'Comentario Multilinea'
    ID = 'ID'
    VAR = 'Palabra Reservada'
    IF = 'Palabra Reservada'
    ELSE = 'Palabra Reservada'
    FOR = 'Palabra Reservada'
    WHILE = 'Palabra Reservada'
    DO = 'Palabra Reservada'
    CONTINUE = 'Palabra Reservada'
    BREAK = 'Palabra Reservada'
    RETURN = 'Palabra Reservada'
    FUNCTION = 'Palabra Reservada'
    CONSTRUCTOR = 'Palabra Reservada'
    CLASS = 'Palabra Reservada'
    NEW = 'Palabra Reservada'
    CONJUNCION = 'Conjuncion'
    DISYUNCION = 'Disyuncion'
    NEGACION = 'Negacion'
    MAS = 'Mas'
    MENOS = 'Menos'
    ASTERISCO = 'Astedisco'
    MAYOR_QUE = 'Mayor Que'
    MENOR_QUE = 'Menor Que'
    PARRENTESIS_IZ = 'Parentesis Izquierdo' 
    PARRENTESIS_DE = 'Parentesis Derecho'
    LLAVE_IZ = 'LLave Izquierdo'
    LLAVE_DE = 'Llave Derecho'
    DIAGONAL = 'Diagonal'
    CORCHETE_IZ = 'Corchete Izquierdo'
    CORCHETE_DE = 'Corchete Derecho'
    DIGITO= 'Digito'
    PUNTO='Punto'
    PUNTO_COMA='Punto y coma'
    CADENA='Cadena'
    ERROR = 'Error caracter Desconocido'

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






