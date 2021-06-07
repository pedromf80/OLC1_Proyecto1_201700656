import os

class Report():
    def __init__(self):
        pass
        #self.__createfiles('salida.html', self.__getHeadHMTL("Archivo html")+self.__getfoothtml())

    def reportjs(self, filenameExt, nameReport, lstoken):
        from Tokenjs import Tipo
        count = 0
        content = '\n<tbody>'
        for token in lstoken:
            if Tipo.ERROR == token.tipoToken:
                count +=1
                content = content+' \n<tr>'
                content = content+' \n<td>'+str(count)+'</td>'
                content = content+' \n<td>'+str(token.fila)+'</td>'
                content = content+' \n<td>'+str(token.columna)+'</td>'
                content = content+' \n<td>El carácter ‘'+token.lexema+'’ no pertenece al lenguaje.</td>'
                content = content+' \n<tr>'
        content = content+' \n</tbody>'
        self.__createfiles(filenameExt, self.__getHeadHMTL(nameReport)+content+self.__getfoothtml())       

    def reportcss(self, filenameExt, nameReport, lstoken):
        from Tokencss import Tipo
        count = 0
        content = '\n<tbody>'
        for token in lstoken:
            if Tipo.ERROR == token.tipoToken:
                count +=1
                content = content+' \n<tr>'
                content = content+' \n<td>'+str(count)+'</td>'
                content = content+' \n<td>'+str(token.fila)+'</td>'
                content = content+' \n<td>'+str(token.columna)+'</td>'
                content = content+' \n<td>El carácter ‘'+token.lexema+'’ no pertenece al lenguaje.</td>'
                content = content+' \n<tr>'
        content = content+' \n</tbody>'
        self.__createfiles(filenameExt, self.__getHeadHMTL(nameReport)+content+self.__getfoothtml())


    def reporthtml(self, filenameExt, nameReport, lstoken):
        from Tokenhtml import Tipo
        count = 0
        content = '\n<tbody>'
        for token in lstoken:
            if Tipo.ERROR == token.tipoToken:
                count +=1
                content = content+' \n<tr>'
                content = content+' \n<td>'+str(count)+'</td>'
                content = content+' \n<td>'+str(token.fila)+'</td>'
                content = content+' \n<td>'+str(token.columna)+'</td>'
                content = content+' \n<td>El carácter ‘'+token.lexema+'’ no pertenece al lenguaje.</td>'
                content = content+' \n<tr>'
        content = content+' \n</tbody>'
        self.__createfiles(filenameExt, self.__getHeadHMTL(nameReport)+content+self.__getfoothtml()) 
    
    def __getHeadHMTL(self, nameReport):
        head = '<!DOCTYPE html>\n<html lang="en">\n<head>n\n<title>'+nameReport+'</title>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js">\n</script>\n<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js">\n</script>\n</head>\n<body>'
        line = ' <div class="container">\n<h2>Reporte '+nameReport+'</h2>\n<table class="table table-bordered">\n<thead class="bg-primary">\n<tr>\n<th>No.</th>\n<th>Linea</th>\n<th>Columna</th>\n<th>Descripcion</th>\n</tr>\n</thead>'
        return head + line
        
    def __getfoothtml(self):
        return '\n</table>\n</div>\n</body>\n</html>'

    def __createfiles(self, filename, content):
        try:
            with open(filename, 'wb') as f:
                f.write(bytes(content, 'UTF-8'))
                f.close()
                os.system('xdg-open '+filename)
        except FileNotFoundError:
            print('FileNotFoundError')
            return "cancelled"
            


