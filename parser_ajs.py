import ply.yacc as yacc
from tokens import Tokens

tokens = Tokens.tokens + Tokens.reserved

###################### INICIO ######################
def p_programa(p):
    '''programa : statement
                | empty'''
    print('programa')
    
def p_empty(p):
    'empty : '


def p_statement(p):
    '''
    statement : content PUNTO_Y_COMA
              | content PUNTO_Y_COMA statement
              | no_semicolon
              | no_semicolon statement
    '''
    print('statement')

def p_content(p):
    '''
    content : define
            | declare
            | assign
    '''
    print('content')

def p_no_semicolon(p):
    '''
    no_semicolon : condition
                 | loop
                 | function_def
    '''
    print('no_semicolon')

###################### HOJAS ######################

def p_bool(p):
    '''bool : TR
            | FL'''
    print('bool')

def p_num(p):
    '''num : ENTERO
           | DECIMAL'''
    print('num')

def p_ident(p):
    '''ident : CADENA_NO_COMILLAS
             | CADENA_COMILLAS
             | CADENA_COMILLAS PUNTO ident
             | CADENA_COMILLAS CORCHETE_ABRE CADENA_NO_COMILLAS CORCHETE_CIERRA
             | CADENA_COMILLAS CORCHETE_ABRE CADENA_NO_COMILLAS CORCHETE_CIERRA indent
             '''
    print('ident')
    
def p_declare(p):
    '''
    declare : LET id
    '''
    print('declare')

def p_id(p):
    '''id : variable
          | variable COMA id
          | variable ASIGNACION valor
          | variable ASIGNACION valor COMA id'''
    print('id')

def p_variable(p):
    '''variable : CADENA_NO_COMILLAS DOS_PUNTOS tipo
                | CADENA_NO_COMILLAS'''
    print('variable')
    
def p_assign(p):
    '''
    assign : variable ASIGNACION valor
    '''
    print('assign')

def p_valor(p):
    '''valor : CADENA_COMILLAS
             | num
             | operacion
             | bool
             | NULL
             | ajson_v
             | CARACTER
             | CADENA_NO_COMILLAS
             | function_call
             | PARENTESIS_ABRE valor PARENTESIS_CIERRA
    '''
    print('valor')

def p_define(p):
    '''
    define : TYPE CADENA_NO_COMILLAS ASIGNACION ajson
    '''
    print('define')

def p_ajson(p):
    '''ajson : LLAVE_ABRE lista LLAVE_CIERRA'''
    print('ajson')

def p_lista(p):
    '''lista : elemento
             | elemento COMA 
             | elemento COMA lista'''
    print('lista')

def p_elemento(p):
    '''elemento : clave DOS_PUNTOS valor_t'''
    print('elemento')

def p_valor_t(p):
    '''valor_t : tipo
               | ajson'''
    print('valor_t')

def p_clave(p):
    '''clave : CADENA_NO_COMILLAS
             | CADENA_COMILLAS'''
    print('clave')

def p_ajson_v(p):
    '''ajson_v : LLAVE_ABRE lista_v LLAVE_CIERRA'''
    print('ajson_v')

def p_lista_v(p):
    '''lista_v : elemento_v
               | elemento_v COMA 
               | elemento_v COMA lista_v'''
    print('lista_v')

def p_elemento_v(p):
    '''elemento_v : clave_v DOS_PUNTOS valor'''
    print('elemento')

def p_clave_v(p):
    '''clave_v : CADENA_NO_COMILLAS
             | CADENA_COMILLAS'''
    print('clave_v')

def p_operacion(p):
    '''operacion : aritmetica
                 | booleana
                 | comparacion
                 | PARENTESIS_ABRE operacion PARENTESIS_CIERRA'''
    print('operacion')
    

def p_aritmetica(p):
    '''aritmetica : valor operador1 valor
                  | valor operador2 valor'''
    print('aritmetica')
    
def p_operador1(p):
    '''operador1 : SUMA
                 | RESTA'''
    print('operador1')
    
def p_operador2(p):
    '''operador2 : MULTIPLICACION
                 | DIVISION'''
    print('operador2')

def p_comparacion(p):
    '''comparacion : valor comparador valor
                   | valor IGUAL valor'''
    print('comparacion')
    
def p_comparador1(p):
    '''comparador : MAYOR 
                  | MENOR 
                  | MAYOR_IGUAL
                  | MENOR_IGUAL
    '''
    print('comparador1')

def p_booleana(p):
    '''booleana : valor comparador2 valor
                | NEGACION valor'''
    print('booleana')
    
def p_comparador2(p):
    '''comparador2 : CONJUNCION
                   | DISYUNCION
    '''
    print('comparador2')


def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | CHARACTER
            | BOOLEAN
            | CADENA_NO_COMILLAS
    '''
    print('tipo')

def p_condition(p):
    '''
    condition : IF PARENTESIS_ABRE expersion PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA
              | IF PARENTESIS_ABRE expersion PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA ELSE LLAVE_ABRE statement LLAVE_CIERRA
    '''
    print('condition')

def p_expersion(p):
    '''
    expersion : valor
              | booleana
              | function_call
    '''
    print('expersion')

def p_loop(p):
    '''
    loop : WHILE PARENTESIS_ABRE expersion PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA
    '''
    print('loop')

def p_function_def(p):
    '''
    function_def : FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE id PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE statement RETURN valor PUNTO_Y_COMA LLAVE_CIERRA
                 | FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE id PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE RETURN valor PUNTO_Y_COMA LLAVE_CIERRA
                 | FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE statement RETURN valor PUNTO_Y_COMA LLAVE_CIERRA
                 | FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE RETURN valor PUNTO_Y_COMA LLAVE_CIERRA
    '''
    print('function_def')

def p_function_call(p):
    '''
    function_call : CADENA_NO_COMILLAS PARENTESIS_ABRE valor PARENTESIS_CIERRA
                  | CADENA_NO_COMILLAS PARENTESIS_ABRE PARENTESIS_CIERRA
    '''
    print('function_call')

def p_error(p):
    if p: print('[ERROR][PARSER] At line: %s' % p)
    else: print('[ERROR][PARSER] At EOF')