
class Lexicojs():
    
    def __init__(self, text):
        self.text = text
        self.lexer_analyzer(self.text)

    def lexer_analyzer(self, text):
        yycolum =0
        xxrow = 0
        self.lexema = ""
        n=0
        ls = list(text)
        for c in ls:
            yycolum +=1
            if n==0: #caso para la transicion de estados
                #print('estado 0')
                if c.isalpha():
                   n =1
                elif c.isdigit():
                    n=2
                elif c =='\"':
                    n=3       
                elif c == '\n':
                   # xxrow +=1
                   # print('line %s' %(xxrow))
                   # print('column %s' %(yycolum))
                   # yycolum =0
                   pass
            elif n ==1:
                #print('estado 1')
                n=0

            elif n == 2:
                #print('estado 2')
                n=0        
            
            elif n == 3:
                print('estado 3')
                n=0