from Analise_Lexica import *
from Analise_Sintatico import *

lexema = lex.lex()
teste = '''i = 1
            while i < 10 do
              i = i + 1
            end'''

lexema.input(teste)
parser = yacc.yacc()
#parser.parse(debug=True)
parser.parse(debug=False)
