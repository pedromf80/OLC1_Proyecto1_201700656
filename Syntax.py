from enum import Enum

# clase enum


class Tipormt(Enum):
    NUMERO = 'Numero'
    SIGNO_MAS = 'Signo Mas'
    SIGNO_MEN = 'Signo Menos'
    SIGNO_POR = 'Signo Multiplicacion'
    SIGNO_DIV = 'Signo Division'
    PARENTESIS_IZQ = 'Parentesis Izquierdo'
    PARENTESIS_DER = 'Parentesis Derecho'
    ID = 'Identificador'
    ERROR = 'Error lexico'
    ULTIMO = 'Fin de ananlisis'

# clase token


class Tokenrmt():
    def __init__(self, tipo, lexema, fila, columna):
        self.tipoToken = tipo
        self.lexema = lexema
        self.fila = fila
        self.columna = columna

# clase Analizador Lexico
class LexicoRmt():
    def __init__(self):
        self.listToken = []
        self.outcodejs = ""

    def lexer_analyzer(self, text):
        self.yycolum = 0
        self.xxrow = 1
        self.lexema = ""
        self.estado = 0
        ls = list(text+"#")
        count = 0
        while (count < ls.__len__()):
            self.yycolum += 1
            c = ls[count]
            count += 1
            if self.estado == 0:
                if c == '+':
                    self.lexema += c
                    self.__addToken(Tipormt.SIGNO_MAS)
                    continue
                elif c == '-':
                    self.lexema += c
                    self.__addToken(Tipormt.SIGNO_MEN)
                    continue
                elif c == '/':
                    self.lexema += c
                    self.__addToken(Tipormt.SIGNO_DIV)
                    continue
                elif c == '*':
                    self.lexema += c
                    self.__addToken(Tipormt.SIGNO_POR)
                    continue
                elif c == '(':
                    self.lexema += c
                    self.__addToken(Tipormt.PARENTESIS_IZQ)
                    continue
                elif c == ')':
                    self.lexema += c
                    self.__addToken(Tipormt.PARENTESIS_DER)
                    continue
                elif c.isdigit():
                    self.lexema += c
                    self.estado = 1
                    continue
                elif c.isalpha():
                    self.lexema +=c
                    self.estado = 4
                    continue
                elif c == '#':
                    self.lexema += c
                    self.__addToken(Tipormt.ULTIMO)
                    #print("fin Analisis lexico")
                    continue
            # aceptacion de numeros
            if self.estado == 1:
                if c.isdigit():
                    self.lexema += c
                    continue
                elif c == '.':
                    self.lexema += c
                    self.estado = 2
                    continue
                else:
                    self.__addToken(Tipormt.NUMERO)
                    count -= 1
                    continue
            if self.estado == 2:
                if c.isdigit():
                    self.lexema += c
                    self.estado = 3
                    continue
                else:
                    self.__addToken(Tipormt.ERROR)
                    count -= 1
                    continue
            if self.estado == 3:
                if c.isdigit():
                    self.lexema += c
                    continue
                else:
                    self.__addToken(Tipormt.NUMERO)
                    count -= 1
                    continue
            # aceptacion de ID
            if self.estado == 4:
                if c.isalpha():
                    self.lexema += c
                    continue
                elif c.isdigit():
                    self.lexema += c
                    continue
                else:
                    self.__addToken(Tipormt.ID)
                    count -= 1
                    continue

    # metodo que genera la lista de tokens encontrados

    def __addToken(self, Tipo):
        self.listToken.append(
            Tokenrmt(Tipo, self.lexema, self.xxrow, self.yycolum))
        self.estado = 0
        self.lexema = ''

    # retorna la lista de tokens
    def getListToken(self):
        return self.listToken

class sintaxAnalixer():
    def __init__(self):
        self.numPreanalisis = None
        self.lstokens = None
    '''
    Gramatica  
    'E->E+T
    'E->E-T
    'E->T
    'T->T*F
    'T->T/F
    'T->F
    'F->(E)
    'F->numero | ID
    
    Esta gramática es recursiva por la izquierda, pero para implementarla necesitamos 
    que la gramática no tenga recursividad por la izuierda, entonces la transformamos 
      
     Gramática que resuelve el problema:     
     
     E-> T EP
     EP-> + T EP
        | - T EP
        | EPSILON
     T-> F TP
     TP-> * F TP
        | / F TP
        | EPSILON
     F->  (E)
        | NUMERO
        | ID     
    Para cada no terminal del lado izquierdo de las producciones, se crea un método
    Para cada no terminal del lado derecho de las producciones, se hace una llamada 
    al método que le corresponde, y para cada terminal del lado derecho se hace una 
    llamada al método match enviando como parámetro el terminal.'''

    def parser(self, tokens):
        self.lstokens = tokens
        self.preanalisis = self.lstokens[0]
        self.numPreanalisis = 0
        self.Accepted = False
        self.__E()
        return self.Accepted

    def __E(self):
        self.__T()
        self.__EP()
        
    def __EP(self):
        if self.preanalisis.tipoToken == Tipormt.SIGNO_MAS:
            self.__match(Tipormt.SIGNO_MAS)
            self.__T()
            self.__EP()
        elif self.preanalisis.tipoToken == Tipormt.SIGNO_MEN:
            self.__match(Tipormt.SIGNO_MEN)
            self.__T()
            self.__EP()    

    def __T(self):
        self.__F()
        self.__TP()

    def __TP(self):
        if self.preanalisis.tipoToken == Tipormt.SIGNO_POR:
            self.__match(Tipormt.SIGNO_POR)
            self.__F()
            self.__TP()

        elif self.preanalisis.tipoToken == Tipormt.SIGNO_DIV:
            self.__match(Tipormt.SIGNO_DIV)
            self.__F()
            self.__TP()    

    def __F(self):
        if self.preanalisis.tipoToken == Tipormt.PARENTESIS_IZQ:
            self.__match(Tipormt.PARENTESIS_IZQ)
            self.__E()
            self.__match(Tipormt.PARENTESIS_DER)
        elif self.preanalisis.tipoToken == Tipormt.NUMERO:
            self.__match(Tipormt.NUMERO)
        else:
            self.__match(Tipormt.ID)

    #metodo match
    def __match(self, tipo):
        if tipo != self.preanalisis.tipoToken:
            print("Se esperaba "+tipo.value)
        elif self.preanalisis.tipoToken != Tipormt.ULTIMO:
            self.numPreanalisis += 1
            self.preanalisis = self.lstokens[self.numPreanalisis]
        elif self.preanalisis.tipoToken == Tipormt.ULTIMO:
            self.Accepted = True
            return





