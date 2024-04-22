import ply.yacc as yacc
from tokens import Tokens

tokens = Tokens.tokens + Tokens.reserved


def p_programa(p):
    '''programa : statement
                | empty'''
    
def p_empty(p):
    'empty : '

def p_statement(p):
    '''
    statement : content PUNTO_Y_COMA
              | content PUNTO_Y_COMA statement
              | no_semicolon
              | no_semicolon statement
    '''

def p_content(p):
    '''
    content : define
            | declare
            | assign
    '''

def p_no_semicolon(p):
    '''
    no_semicolon : condition
                 | loop
                 | function_def
    '''

def p_define(p):
    '''
    define : TYPE CADENA_NO_COMILLAS ASIGNACION ajson
    '''

def p_ajson(p):
    '''ajson : LLAVE_ABRE lista LLAVE_CIERRA
             | LLAVE_ABRE LLAVE_CIERRA'''

def p_lista(p):
    '''lista : elemento
             | elemento COMA 
             | elemento COMA lista'''

def p_elemento(p):
    '''elemento : clave DOS_PUNTOS valor_t'''

def p_clave(p):
    '''clave : CADENA_NO_COMILLAS
             | CADENA_COMILLAS'''

def p_valor_t(p):
    '''valor_t : CADENA_COMILLAS
                | num
                | operacion
                | bool
                | NULL
                | ajson
                | tipo
                | CARACTER
                | CADENA_NO_COMILLAS
    '''

def p_operacion(p):
    '''operacion : aritmetica
                 | booleana
                 | comparacion
                 | PARENTESIS_ABRE operacion PARENTESIS_CIERRA'''
    

def p_aritmetica(p):
    '''aritmetica : ex operador1 ex
                  | ex2 operador2 ex2'''
    
def p_operador1(p):
    '''operador1 : SUMA
                 | RESTA'''
    
def p_operador2(p):
    '''operador2 : MULTIPLICACION
                 | DIVISION'''
    
def p_comparacion(p):
    '''comparacion : ex comparador ex
                   | ex1 IGUAL ex1'''
    
def p_comparador1(p):
    '''comparador : MAYOR 
                  | MENOR 
                  | MAYOR_IGUAL
                  | MENOR_IGUAL
    '''
def p_booleana(p):
    '''booleana : ex3 comparador2 ex3
                | NEGACION ex3'''
    
def p_comparador2(p):
    '''comparador2 : CONJUNCION
                   | DISYUNCION
    '''
def p_ex(p):
    '''ex : num
          | CHARACTER
          | CADENA_NO_COMILLAS
          | aritmetica
          | comparacion
          | PARENTESIS_ABRE ex PARENTESIS_CIERRA'''

def p_ex1(p):
    '''ex1 : ex
           | bool
           | booleana
           | aritmetica
           | comparacion
           | PARENTESIS_ABRE ex1 PARENTESIS_CIERRA'''

def p_ex2(p):
    '''ex2 : num
           | CADENA_NO_COMILLAS
           | aritmetica
           | PARENTESIS_ABRE ex2 PARENTESIS_CIERRA'''

def p_ex3(p):
    '''ex3 : bool
           | CADENA_NO_COMILLAS
           | comparacion
           | PARENTESIS_ABRE ex3 PARENTESIS_CIERRA'''
    
def p_bool(p):
    '''bool : TR
            | FL'''

def p_num(p):
    '''num : ENTERO
           | DECIMAL'''

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | CHARACTER
            | BOOLEAN
            | CADENA_NO_COMILLAS
    '''

def p_declare(p):
    '''
    declare : LET id
    '''

def p_id(p):
    '''id : variable
          | variable COMA id'''

def p_variable(p):
    '''variable : CADENA_NO_COMILLAS DOS_PUNTOS tipo
                | CADENA_NO_COMILLAS'''
    
def p_assign(p):
    '''
    assign : variable ASIGNACION valor
    '''

def p_valor(p):
    '''valor : CADENA_COMILLAS
             | num
             | operacion
             | bool
             | NULL
             | ajson
             | CARACTER
             | CADENA_NO_COMILLAS
             | function_call
    '''

def p_condition(p):
    '''
    condition : IF PARENTESIS_ABRE expersion PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA
              | IF PARENTESIS_ABRE expersion PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA ELSE LLAVE_ABRE statement LLAVE_CIERRA
    '''

def p_expersion(p):
    '''
    expersion : ex3
              | booleana
              | function_call
    '''

def p_loop(p):
    '''
    loop : WHILE PARENTESIS_ABRE expersion PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA
    '''

def p_function_def(p):
    '''
    function_def : FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE id PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE statement RETURN valor PUNTO_Y_COMA LLAVE_CIERRA
                 | FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE id PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE RETURN valor PUNTO_Y_COMA LLAVE_CIERRA
                 | FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE statement RETURN valor PUNTO_Y_COMA LLAVE_CIERRA
                 | FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE RETURN valor PUNTO_Y_COMA LLAVE_CIERRA
    '''

def p_function_call(p):
    '''
    function_call : CADENA_NO_COMILLAS PARENTESIS_ABRE valor PARENTESIS_CIERRA
                  | CADENA_NO_COMILLAS PARENTESIS_ABRE PARENTESIS_CIERRA
    '''

def p_error(p):
    if p: print('[ERROR][PARSER] At line: %s' % p)
    else: print('[ERROR][PARSER] At EOF')