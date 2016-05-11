import ply.lex as lexer

tokens = ["NAME", "ID", "SAL", "DATE", "EMAIL"]


t_ignore = ' \t'
t_NAME = r'[a-zA-Z]+'
t_ID = r'[\d+]+'
t_SAL = r'\d+\.\d+'
t_DATE = r'\d+/[a-zA-Z]+/\d+'
t_EMAIL = r'\w+\.\w+@\w+\.edu'

def t_error(t):
    print('Illegal character %s', t.value[0])
    t.lexer.skip(1)
    return t


lexer.lex()