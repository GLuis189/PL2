import ply.yacc as yacc
from tokens import Tokens
import json


def convert_keys_to_strings(d):
    if isinstance(d, dict):
        new_dict = {}
        for k, v in d.items():
            new_key = str(k) if isinstance(k, tuple) else k
            new_dict[new_key] = convert_keys_to_strings(v)
        return new_dict
    elif isinstance(d, list):
        return [convert_keys_to_strings(item) for item in d]
    else:
        return d

def cargar_symbolos():
    with open('tables.out', 'w') as f:
        f.write('Symbols:\n')
        f.write(json.dumps(convert_keys_to_strings(symbols), indent=4))
        f.write('\n')
        f.write('Objects:\n')
        f.write(json.dumps(convert_keys_to_strings(objects), indent=4))

tokens = Tokens.tokens + Tokens.reserved

symbols = {}
objects = {}

precedence = (
        ('left', 'CONJUNCION', 'DISYUNCION'),
        ('right', 'NEGACION'),
        ('nonassoc', 'IGUAL'),
        ('nonassoc', 'MENOR_IGUAL', 'MENOR', 'MAYOR_IGUAL', 'MAYOR'),
        ('left', 'SUMA', 'RESTA'),
        ('left', 'MULTIPLICACION', 'DIVISION'),
        ('right', 'UPLUS', 'UMINUS')
    )
###################### INICIO ######################
def p_programa(p):
    '''programa : statement
                | empty'''
    #print('programa')
    cargar_symbolos()
    
def p_empty(p):
    '''empty : '''
    #print('empty')
    p[0] = None

def p_statement(p):
    '''
    statement : content PUNTO_Y_COMA
              | content PUNTO_Y_COMA statement
              | no_semicolon
              | no_semicolon statement
    '''
    #print('statement')

def p_content(p):
    '''
    content : define
            | declare
            | assign
    '''
    #print('content')

def p_no_semicolon(p):
    '''
    no_semicolon : condition
                 | loop
                 | function_def
    '''
    #print('no_semicolon')

def p_ident(p):
    '''ident : CADENA_NO_COMILLAS
             | CADENA_NO_COMILLAS PUNTO ident
             | CADENA_NO_COMILLAS CORCHETE_ABRE CADENA_COMILLAS CORCHETE_CIERRA
             | CADENA_NO_COMILLAS CORCHETE_ABRE CADENA_COMILLAS CORCHETE_CIERRA PUNTO ident
             '''
    p[0] = p[1]

###################### DECLARACIONES ######################

def p_declare(p):
    '''
    declare : LET id asign_valor
    '''
    #print('declare')
    lista_vars = p[2]
    tipo_a, value = p[3]
    if isinstance(p[3], dict):
        value = p[3]
    for var in lista_vars:
        tipo, name = var
        if name in symbols:
            print('[ERROR][PARSER] Variable %s already declared' % name)
        else:
            if tipo == None or tipo == tipo_a:
                symbols[name] = (tipo_a, value)
            else:
                if tipo in objects:
                   symbols[name] = (tipo, value)
    

def p_asign_valor(p):
    '''
    asign_valor : ASIGNACION valor
                | empty
    '''
    #print('asign_valor')
    if len(p) > 2: p[0] = p[2]
    else: p[0] = (None, p[1])

def p_id(p):
    '''id : variable'''
    #print('id')
    p[0] = [p[1]]

def p_id_varios(p):
    '''id : variable COMA id'''
    # print('id_varios')
    ultimo = p[1]
    resto = p[3]
    p[0] = [ultimo] + resto
    

def p_variable(p): 
    '''variable : ident
                | ident DOS_PUNTOS CADENA_NO_COMILLAS'''
    # print('variable')
    if len(p) == 2: p[0] = (None, p[1])
    else:
        # Para hacer, comprobar que el tipo (cadena no comillas) sea valido
        if p[3] not in objects:
            print('[ERROR][PARSER] Type %s not defined' % p[3])
        else:
            p[0] = (p[3], p[1])
            
###################### ASIGNACIONES ######################
    
def p_assign(p):
    '''
    assign : ident asign_valor
    '''
    # print('assign')
    ident = p[1]
    if isinstance(ident, list):
        for i in ident:
            if i in symbols:
                tipo, value = p[2]
                if tipo == symbols[i][0]:
                    symbols[i] = (tipo, value)
                else:
                    print('[ERROR][PARSER] Type mismatch in variable %s' % i)
            else:
                print('[ERROR][PARSER] Variable %s not declared' % i)
    else:
        if ident in symbols:
            tipo, value = p[2]
            tipo_s= symbols[ident][0]
            symbols[ident] = (tipo, value)
            # Comprobaciones de tipo pero no se si es necesario #######################################################################################
            # if tipo == tipo_s or tipo_s == None:
            #     symbols[ident] = (tipo, value)
            # else:
            #     if tipo == 'int' and tipo_s == 'float':
            #         symbols[ident] = (tipo, value)
            #     elif tipo == 'char' and tipo_s == 'int':
            #         symbols[ident] = (tipo_s, value.encode('utf-8'))
            #     else:
            #         print('[ERROR][PARSER] Type mismatch in variable %s' % ident)
        else:
            print('[ERROR][PARSER] Variable %s not declared' % ident)

# def p_valor(p):
#     '''valor : ident
#              | ENTERO
#              | DECIMAL
#              | operacion
#              | v_bool
#              | NULL
#              | ajson_v
#              | CARACTER
#              | function_call
#              | PARENTESIS_ABRE valor PARENTESIS_CIERRA
#              | SUMA valor %prec UPLUS
#              | RESTA valor %prec UMINUS
#     '''
#     #print('valor')

def p_valor(p):
    '''valor : operacion
             | ajson_v
             | function_call'''
    p[0] = p[1]

def p_valor_ident(p):
    '''valor : ident'''
    #print('valor_ident')
    ident = p[1]
    if ident in symbols:
        p[0] = symbols[ident]

def p_valor_entero(p):
    '''valor : ENTERO'''
    #print('valor_entero')

    p[0] = ('int', p[1])

def p_valor_decimal(p):
    '''valor : DECIMAL'''
    #print('valor_decimal')
    p[0] = ('float', p[1])

def p_valor_bool(p):
    '''valor : TR
              | FL'''
    #print('valor_bool')
    p[0] = ('bool', p[1])

def p_valor_null(p):
    '''valor : NULL'''
    #print('valor_null')
    p[0] = ('null', p[1])

def p_valor_caracter(p):
    '''valor : CARACTER'''
    #print('valor_caracter')
    p[0] = ('char', p[1])

def p_valor_parentesis(p):
    '''valor : PARENTESIS_ABRE valor PARENTESIS_CIERRA'''
    #print('valor_parentesis')
    p[0] = p[2]

def p_valor_unary(p):
    '''valor : SUMA valor %prec UPLUS
             | RESTA valor %prec UMINUS
    '''
    #print('valor_unary')
    tipo, valor = p[2]
    signo = p[1]
    if signo == '-': valor = -valor
    p[0] = (tipo, valor)


def p_define(p):
    '''
    define : TYPE CADENA_NO_COMILLAS ASIGNACION ajson
    '''
    # print('define')
    name = p[2]
    if name in objects:
        print('[ERROR][PARSER] Object %s already defined' % name)
    else:
        objects[name] = p[4]

def p_ajson(p):
    '''ajson : LLAVE_ABRE lista LLAVE_CIERRA'''
    #print('ajson')
    p[0] = p[2]

def p_lista(p):
    '''lista : elemento
             | elemento COMA 
             | elemento COMA lista'''
    #print('lista')
    if len(p) <= 3: p[0] = p[1]
    else: p[0] = p[1] | p[3]

def p_elemento(p):
    '''elemento : clave DOS_PUNTOS valor_t'''
    #print('elemento')
    p[0] = {p[1]: p[3]}

def p_valor_t(p):
    '''valor_t : tipo
               | ajson'''
    #print('valor_t')
    p[0] = p[1]

# Hay dos tipos de claves, sin comillas que se pueden acceder con punto #####################################################################33
# y corchete, y con comillas que solo se pueden acceder con corchetes
# para eso lo codifico como una tupla (key, tipo) 
# siendo tipo 0 si es sin comillas y 1 si es con comillas

# def p_clave(p):
#     '''clave : CADENA_NO_COMILLAS
#              | CADENA_COMILLAS'''
#     #print('clave')

def p_clave_comillas(p):
    '''clave : CADENA_COMILLAS'''
    #print('clave_comillas')
    p[0] = (p[1], 0)

def p_clave_no_comillas(p):
    '''clave : CADENA_NO_COMILLAS'''
    #print('clave_no_comillas')
    p[0] = (p[1], 1)


def p_ajson_v(p):
    '''ajson_v : LLAVE_ABRE lista_v LLAVE_CIERRA'''
    #print('ajson_v')
    p[0] = p[2]

def p_lista_v(p):
    '''lista_v : elemento_v
               | elemento_v COMA 
               | elemento_v COMA lista_v'''
    #print('lista_v')
    if len(p) <= 3: p[0] = p[1]
    else: p[0] = p[1] | p[3]

def p_elemento_v(p):
    '''elemento_v : clave_v DOS_PUNTOS valor'''
    #print('elemento')
    p[0] = {p[1]: p[3]}

def p_clave_v(p):
    '''clave_v : CADENA_NO_COMILLAS
               | CADENA_COMILLAS'''
    #print('clave_v')
    p[0] = p[1]

def p_operacion(p):
    '''operacion : aritmetica
                 | booleana
                 | comparacion'''
    #print('operacion')
    

def p_aritmetica(p):
    '''aritmetica : valor SUMA valor %prec SUMA
                  | valor RESTA valor %prec RESTA
                  | valor MULTIPLICACION valor %prec MULTIPLICACION
                  | valor DIVISION valor %prec DIVISION'''
    #print('aritmetica')
    

def p_comparacion(p):
    '''comparacion : valor MAYOR valor %prec MAYOR
                   | valor MENOR valor %prec MENOR
                   | valor MAYOR_IGUAL valor %prec MAYOR_IGUAL
                   | valor MENOR_IGUAL valor %prec MENOR_IGUAL
                   | valor IGUAL valor %prec IGUAL'''
    #print('comparacion')

def p_booleana(p):
    '''booleana : valor CONJUNCION valor %prec CONJUNCION
                | valor DISYUNCION valor %prec DISYUNCION
                | NEGACION valor %prec NEGACION'''
    #print('booleana')

# def p_tipo(p):
#     '''tipo : INT
#             | FLOAT
#             | CHARACTER
#             | BOOLEAN
#             | CADENA_NO_COMILLAS
#     '''
#     #print('tipo')

def p_tipo_entero(p):
    '''tipo : INT'''
    #print('tipo_entero')
    p[0] = 'int'

def p_tipo_decimal(p):
    '''tipo : FLOAT'''
    #print('tipo_decimal')
    p[0] = 'float'

def p_tipo_caracter(p):
    '''tipo : CHARACTER'''
    #print('tipo_caracter')
    p[0] = 'char'

def p_tipo_booleano(p):
    '''tipo : BOOLEAN'''
    #print('tipo_booleano')
    p[0] = 'bool'

def p_tipo_cadena(p):
    '''tipo : CADENA_NO_COMILLAS'''
    #print('tipo_cadena')
    if p[1] not in objects:
        print('[ERROR][PARSER] Type %s not defined' % p[1])
    else:
        p[0] = p[1]

def p_condition(p):
    '''
    condition : IF PARENTESIS_ABRE valor PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA
              | IF PARENTESIS_ABRE valor PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA ELSE LLAVE_ABRE statement LLAVE_CIERRA
    '''
    #print('condition')

def p_loop(p):
    '''
    loop : WHILE PARENTESIS_ABRE valor PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA
    '''
    #print('loop')

def p_id_t(p):
    '''id_t : variable_t
            | variable_t COMA id_t
            | empty'''
    #print('id_t')

def p_variable_t(p):
    '''variable_t : CADENA_NO_COMILLAS DOS_PUNTOS tipo
    '''

    #print('variable_t')

def p_function_def(p):
    '''
    function_def : FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE id_t PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE statement RETURN valor PUNTO_Y_COMA LLAVE_CIERRA
                 | FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE id_t PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE RETURN valor PUNTO_Y_COMA LLAVE_CIERRA
    '''
    #print('function_def')

def p_function_call(p):
    '''
    function_call : CADENA_NO_COMILLAS PARENTESIS_ABRE arg PARENTESIS_CIERRA
    '''
    #print('function_call')

def p_arg(p):
    '''arg : valor
           | valor COMA arg
           | empty'''
    #print('arg')

def p_error(p):
    error = True
    if p: print('[ERROR][PARSER] At line: %s' % p)
    else: print('[ERROR][PARSER] At EOF')

