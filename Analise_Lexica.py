import ply.lex as lex

reserved = {
    'and': 'AND',
    'end': 'END',
    'in': 'IN',
    'break': 'BREAK',
    'false': 'FALSE',
    'local': 'LOCAL',
    'return': 'RETURN',
    'do': 'DO',
    'for': 'FOR',
    'nil': 'NIL',
    'then': 'THEN',
    'else': 'ELSE',
    'function': 'FUNCTION',
    'elseif': 'ELSEIF',
    'not': 'NOT',
    'true': 'TRUE',
    'if': 'IF',
    'or': 'OR',
    'while': 'WHILE',
}
tokens = [
    'SUM', 'SUB', 'MULT', 'DIV', 'DIV_INT', 'MODULE', 'POW', 'EQUAL', 'ASSIGN',
    'DIF', 'LESS_THAN', 'BIGGER_THAN', 'BIGGER_EQUAL', 'LESS_EQUAL',
    'BITWISE_AND', 'BITWISE_OR', 'DENIAL', 'BITWISE_EXC_OR',
    'UNARY_BITWISE_NOT', 'ID', 'COMMA', 'LPAREN', 'RPAREN', 'LKEY', 'RKEY',
    'LCOCHETE', 'RCOCHETE', 'NUMBER', 'DOT', 'SEMICOLON', 'COLON', 'COMMENT',
    'CONCATENATION', 'LENGHT', 'STRING', 'NEWLINE'
] + list(reserved.values())
#concatenation
t_SUM = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_DIV_INT = r'//'
t_MODULE = r'%'
t_POW = r'\^'
t_EQUAL = r'=='
t_ASSIGN = r'='
t_DIF = r'~='
t_LESS_THAN = r'<'
t_BIGGER_THAN = r'>'
t_BIGGER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_BITWISE_AND = r'&'
t_BITWISE_OR = r'\|'
t_LENGHT = r'\#'
t_DENIAL = r'-'
t_BITWISE_EXC_OR = r'~' 
t_UNARY_BITWISE_NOT = r'~'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCOCHETE = r'\['
t_RCOCHETE = r'\]'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_DOT = r'\.'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_COLON = r'\:'
#--[[ --]]
t_COMMENT = r'(--\[\[(.|\n)*?--\]\])|(--.*)'
t_CONCATENATION = r'\.\.'
t_STRING = r'\"([^\\\n]|(\\.))*?\"'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_NEWLINE(t):
    r'\n\s*'
    t.lexer.lineno += len(t.value)
    return t


t_ignore = ' \t'


def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

lexer.input(
    "1234567 \n 8 = 90 .. 9A \n +.;:,-* \n /|[]{}qwer \n ty\"uiop\"kjhgf \n asdzxcvbn ? m==)("
)
for token in lexer:
    print(token.type, token.value, token.lineno, token.lexpos)

while True:
    tok = lexer.token()

    if not tok: break
#  Use token
