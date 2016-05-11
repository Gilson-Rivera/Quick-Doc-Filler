import ply.yacc as yacc
from openpyxl import load_workbook

from DB import Lex
from DB.Database import *
from DB.TempHandler import *

tokens = Lex.tokens
db = Database
th = TempHandler


def p_program(p):
    """
    program : statement
    """


def p_statement(p):
    """
    statement : command NAME ID SAL NAME DATE NAME
                | command NAME ID NAME
                | command EMAIL NAME
                | command param
                | command
    """
    try:
        if p[1] == 'add':
           print(db.add(db, p[2], p[3], p[4], p[5], p[6], p[7]))
        elif p[1] == 'edit':
            print(db.edit(db, p[2], p[3], p[4]))
        elif p[1] == 'delete':
            print(db.delete(db, p[2]))
        elif p[1] =='generate':
            print(th.Generate(th,p[2],p[3],p[4]))
        elif p[1] == 'print':
            print(th.printDoc(th,p[2]))
        elif p[1] == 'email':
            print(th.emailDoc(th,p[2],p[3]))
        elif p[1] == 'help':
            db.help(db)
    except:
        print('Invalid Command Parameters')


#Utilize add como si fuera un NAME. La idea es algo parecido al interpreter
def p_command_add(p):
    """
    command : NAME
    """
    p[0] = p[1]


def p_param(p):
    """
    param : NAME
            | ID
    """
    p[0] = p[1]


def p_error(p):
    print("Invalid Parameter Syntax")



parser = yacc.yacc()
print('Welcome to Quick Doc Filler!\n'
      'For some instructions, please type "help".')
while True:
    try:
        i = input('QDF>')
    except EOFError:
        break
    if not i:
        continue
    elif i == 'exit':
        break
    try:
        parser.parse(i)
    except SyntaxError:
        print('Invalid syntax')





