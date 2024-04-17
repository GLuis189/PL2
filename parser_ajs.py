import ply.yacc as yacc
from tokens import Tokens

tokens = Tokens.tokens + Tokens.reserved

def p_programa(p):
    '''programa : statement
                | empty'''

def p_statement(p):
    '''
    statement : content SEMICOLON
              | content SEMICOLON statement
    '''


    


    
