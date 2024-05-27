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
    elif isinstance(d, tuple):
        return [d[0],convert_keys_to_strings(d[1])]
    else:
        return d

def cargar_symbolos():
    with open('tables.out', 'w') as f:
        f.write('Symbols:\n')
        f.write(json.dumps(convert_keys_to_strings(symbols), indent=4))
        f.write('\n')
        f.write('Registros:\n')
        f.write(json.dumps(convert_keys_to_strings(registros), indent=4))
        f.write('\n')
        f.write('Objects:\n')
        f.write(json.dumps(convert_keys_to_strings(objects), indent=4))
        f.write('\n')
        f.write('Functions:\n')
        f.write(json.dumps(convert_keys_to_strings(functions), indent=4))

tokens = Tokens.tokens + Tokens.reserved

symbols = {}
registros = {}
objects = {}
functions = {}

precedence = (
        ('left', 'DISYUNCION'),
        ('left', 'CONJUNCION'),
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

def p_ident_simple(p):
    '''ident : CADENA_NO_COMILLAS
             | CADENA_NO_COMILLAS CORCHETE_ABRE CADENA_COMILLAS CORCHETE_CIERRA
             '''
    # p[0] = p[1]
    if len(p) == 2: p[0] = [(p[1], 1)]
    else : p[0] = [(p[1], 1), (p[3], 0)]

   
    

def p_ident_recurivo(p):
    '''ident : CADENA_NO_COMILLAS PUNTO ident
             | CADENA_NO_COMILLAS CORCHETE_ABRE CADENA_COMILLAS CORCHETE_CIERRA PUNTO ident
    '''
    # p[0] = p[1]
    if len(p) == 4: p[0] = [(p[1], 1)] + p[3]
    else: p[0] = [(p[1], 1), (p[3], 0)] + p[6]

###################### DECLARACIONES ######################

def p_declare(p):
    '''

        declare : LET id 
    '''
    #print('declare')
    lista_vars = p[2]
    for i in range(len(lista_vars)):
        if i%2 == 0:
            if isinstance(p[2][i+1], dict):
                tipo_a = None
                value = p[2][i+1]
            else:
                if p[2][i+1] != None:
                    tipo_a, value = p[2][i+1]
                else:
                    tipo_a = None
                    value = p[2][i+1]
            tipo, name = p[2][i]
            name = name[0]
            if name in symbols:
                print('[ERROR][PARSER] Variable %s already declared' % name[0])
            else:
                if tipo == tipo_a or tipo == None:
                    symbols[name] = (tipo_a, value)
                else:
                    if tipo in objects:
                        coincide = True
                        if value:
                            c = 0
                            while c ==0:
                        #recorremos el diccionario comprobando el tipo
                                for clave_registro, clave_objeto, clave_llave in zip(list(p[2][i+1].values()), list(objects[tipo].values()), list(p[2][i+1].keys())):
                                    if isinstance(clave_objeto, dict):
                                        if isinstance(clave_registro, dict):
                                            pass
                                        else:
                                             coincide = False
                                             print("[ERROR][PARSER] Type mismatch,  %s it´s not a dict %" % (clave_registro[0]))
                                    elif clave_registro[0] != clave_objeto:
                                        if clave_objeto == 'float':
                                            if clave_registro[0] == 'int':
                                                value[clave_llave] = ('float' , float(value[clave_llave][1]))
                                            elif clave_registro[0] == 'char':
                                                value[clave_llave] = ('float' , float(ord(value[clave_llave][1])))
                                            else:
                                                coincide = False
                                                print("[ERROR][PARSER] Type mismatch, can't covert %s to %s" % (clave_registro[0], clave_objeto))
                                        elif clave_objeto == 'int':
                                            if clave_registro[0] == 'char':
                                                value[clave_llave] = ('int' , ord(value[clave_llave][1]))
                                            else:
                                                coincide = False
                                                print("[ERROR][PARSER] Type mismatch, can't covert %s to %s" % (clave_registro[0], clave_objeto))
                                        else:
                                            coincide = False
                                            print("[ERROR][PARSER] Type mismatch, can't covert %s to %s" % (clave_registro[0], clave_objeto))
                                c-= 1
                        if coincide and len(list(p[2][i+1].values())) == len(list(objects[tipo].values())):
                            registros[name] = (tipo, value)
                        else:
                            print("[ERROR][PARSER]Type mismatch, the given assignment %s does not match the object %s " % (name[0],tipo))
             
                            

def p_asign_valor(p):
    '''
    asign_valor : ASIGNACION valor
                | empty
    '''
    #print('asign_valor')
    if len(p) > 2: p[0] = p[2]
    else: p[0] = (None, p[1])
    '''def recorrer_diccionario(diccionario):
        if isinstance(diccionario, dict):
            for clave, valor in diccionario.items():
                if isinstance(valor, dict):
                    recorrer_diccionario(valor)
                    print(valor,'TOMATEEEEEEEEE')
                    print(clave)
                else:
                    pass
    recorrer_diccionario(p[2])'''
    
    



def p_id(p):
    '''id : variable asign_valor'''
    #print('id')
    p[0] = [p[1], p[2]]
    

def p_id_varios(p):
    '''id : variable asign_valor COMA id'''
    # print('id_varios')
    ultimo = p[1]
    valor = p[2]
    resto = p[4]
    p[0] = [ultimo, valor] + resto

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
    def asignar_valor(clave, regist, value):
        if len(clave) == 1 :
            regist[clave[0]] = value
            return regist
        elif isinstance(regist[clave[0]], dict):
            regist[clave[0]] = asignar_valor(clave[1:], regist[clave[0]], value)
            return regist
        elif isinstance(regist[clave[0]], tuple):
            regist[clave[0]] = (regist[clave[0]][0], asignar_valor(clave[1:], regist[clave[0]][1], value))
            return regist
        else:
            pass

    ident = p[1]
    if len(ident) == 1:
        ident = ident[0]
    if isinstance(ident, list):
        #build-up registros
        Registros = asignar_valor(ident, registros, p[2])
    else:
        if ident in symbols:
            if isinstance(p[2], dict) or not p[2]:
                    symbols[ident] = (symbols[ident][0],p[2])
            else:
                tipo, value = p[2]
                #tipo_s= symbols[ident][0]
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
        elif ident in registros:
            if isinstance(p[2], tuple) or not p[2]:
                registros[ident] = p[2]
            elif isinstance(p[2], dict):
                if registros[ident][0] in objects:
                        coincide = True
                        c = 0
                        tipo = registros[ident][0]
                        value = p[2]
                        while c == 0:
                        #recorremos el diccionario comprobando el tipo
                            for clave_registro, clave_objeto, clave_llave in zip(list(value.values()), list(objects[tipo].values()), list(p[2].keys())):
                                    if isinstance(clave_objeto, dict):
                                        if isinstance(clave_registro, dict):
                                            pass
                                        else:
                                             coincide = False
                                             print("[ERROR][PARSER] Type mismatch,  %s it´s not a dict %" % (clave_registro[0]))
                                    elif clave_registro[0] != clave_objeto:
                                        if clave_objeto == 'float':
                                            if clave_registro[0] == 'int':
                                                value[clave_llave] = ('float' , float(value[clave_llave][1]))
                                            elif clave_registro[0] == 'char':
                                                value[clave_llave] = ('float' , float(ord(value[clave_llave][1])))
                                            else:
                                                coincide = False
                                                print("[ERROR][PARSER] Type mismatch, can't covert %s to %s" % (clave_registro[0], clave_objeto))
                                        elif clave_objeto == 'int':
                                            if clave_registro[0] == 'char':
                                                value[clave_llave] = ('int' , ord(value[clave_llave][1]))
                                            else:
                                                coincide = False
                                                print("[ERROR][PARSER] Type mismatch, can't covert %s to %s" % (clave_registro[0], clave_objeto))
                                        else:
                                            coincide = False
                                            print("[ERROR][PARSER] Type mismatch, can't covert %s to %s" % (clave_registro[0], clave_objeto))
                            c-= 1
                        if coincide and len(list(value.values())) == len(list(objects[tipo].values())):
                           registros[ident] = (registros[ident][0],p[2])
                        else:
                            print("[ERROR][PARSER]Type mismatch, the given assignment %s does not match the object %s " % (ident[0],registros[ident][0]))
            else:
                print('[ERROR][PARSER] object %s cannot be assigned' % ident[0])
            
        elif ident in functions:
            print('[ERROR][PARSER] Function %s cannot be assigned' % ident[0])
        else:
            print('[ERROR][PARSER] Variable %s not declared' % ident[0])
   

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
    if len(p[1]) == 1:
        ident = p[1][0]
        if ident in symbols:
            p[0] = symbols[ident]
        elif ident in registros:
            p[0] = registros[ident]
    else:
        aux = registros
        for i in range(len(p[1])):
            name = p[1][i]
            clave_num = 1
            if ((name[0],1) in aux) or ((name[0], 0) in aux):
                if name[1] == 0:
                    if ((name[0], 0)) in aux:
                        clave_num = 0
                    if i == 0:
                        aux = aux[(name[0], clave_num)][1]
                    else:
                        if i == len(p[1]) - 1:
                            p[0] = aux[(name[0], clave_num)] 
                        else:
                            aux = aux[(name[0], clave_num)]
                else:
                    if ((name[0], 0)) in aux:
                        print('[ERROR][PARSER] Misuse of the point with attribute %s' % name[0])
                        break
                    if i == 0:
                        aux = aux[name][1]
                    else:
                        if i == len(p[1]) - 1:
                            p[0] = aux[name]
                            
                        else:
                            aux = aux[name]   
            else:
                print('[ERROR][PARSER] Attribute %s not declared' % name[0])
                break
    

        


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

def p_clave_v_comillas(p):
    '''clave_v : CADENA_COMILLAS'''
    #print('clave_comillas')
    p[0] = (p[1], 0)
   

def p_clave_v_no_comillas(p):
    '''clave_v : CADENA_NO_COMILLAS'''
    #print('clave_no_comillas')
    p[0] = (p[1], 1)

def p_operacion(p):
    '''operacion : aritmetica
                 | booleana
                 | comparacion'''
    #print('operacion')
    p[0] = p[1]

def p_aritmetica_suma_resta(p):
    '''aritmetica : valor SUMA valor %prec SUMA
                  | valor RESTA valor %prec RESTA'''
    #print('aritmetica')
    if p[1] and p[2]:
        t1, v1 = p[1]
        t2, v2 = p[3]
        op = p[2]
    else:
        print('[ERROR][PARSER] Not declared variable')
        t1= p[1]
        t2 = p[3]
    if t1 in ['int', 'float', 'char'] and t2 in ['int', 'float', 'char']:
        if t1 == t2:
            if op == '+': p[0] = (t1, v1 + v2)
            else: p[0] = (t1, v1 - v2)
        #int -> float
        elif t1 == 'int' and t2 == 'float' or t1 == 'float' and t2 == 'int':
            if op == '+': p[0] = ('float', v1 + v2)
            else: p[0] = ('float', v1 - v2)
        #char -> int
        elif t1 == 'char' and t2 == 'int':
            if op == '+': p[0] = ('int', ord(v1) + v2)
            else: p[0] = p[0] = ('int', ord(v1) - v2)
        elif t1 == 'int' and t2 == 'char':
            if op == '+': p[0] = ('int', v1 + ord(v2))
            else: p[0] = ('int', v1 - ord(v2))
        #char -> float
        elif t1 == 'char' and t2 == 'float':
            if op == '+': p[0] = ('float', ord(v1) + v2)
            else: p[0] = p[0] = ('float', ord(v1) - v2)
        elif t1 == 'float' and t2 == 'char':
            if op == '+': p[0] = ('float', v1 + ord(v2))
            else: p[0] = ('float', v1 - ord(v2))
    else:
        print('[ERROR][PARSER] Type mismatch in arithmetic operation')

def p_aritmetica_mul_div(p):
    '''aritmetica : valor MULTIPLICACION valor %prec MULTIPLICACION
                  | valor DIVISION valor %prec DIVISION'''
    #print('aritmetica')
    if p[1] and p[2]:
        t1, v1 = p[1]
        t2, v2 = p[3]
        op = p[2]
    else:
        print('[ERROR][PARSER] Not declared variable')
        t1= p[1]
        t2 = p[3]
    if t1 in ['int', 'float'] and t2 in ['int', 'float']:
        if t1 == t2:
            if op == '*': p[0] = (t1, v1 * v2)
            else:
                if v2 != 0: p[0] = (t1, v1 / v2)
                else: print('[ERROR][PARSER] Division by zero')
        elif t1 == 'int' and t2 == 'float' or t1 == 'float' and t2 == 'int':
            if op == '*': p[0] = ('float', v1 * v2)
            elif op == '/':
                if v2 != 0: p[0] = ('float', v1 / v2)
                else: print('[ERROR][PARSER] Division by zero')
    else:
        print('[ERROR][PARSER] Type mismatch in arithmetic operation')
    

def p_comparacion(p):
    '''comparacion : valor MAYOR valor %prec MAYOR
                   | valor MENOR valor %prec MENOR
                   | valor MAYOR_IGUAL valor %prec MAYOR_IGUAL
                   | valor MENOR_IGUAL valor %prec MENOR_IGUAL'''
    #print('comparacion')
    t1, v1 = p[1]
    t2, v2 = p[3]
    op = p[2]
    if t1 in ['int', 'float', 'char'] and t2 in ['int', 'float', 'char']:
        if t1 == t2 or (t1 == 'int' and t2 == 'float' or t1 == 'float' and t2 == 'int'):
            if op == '>': p[0] = ('bool', v1 > v2)
            elif op == '<': p[0] = ('bool', v1 < v2)
            elif op == '>=': p[0] = ('bool', v1 >= v2)
            elif op == '<=': p[0] = ('bool', v1 <= v2)
    else:
        print('[ERROR][PARSER] Type mismatch in comparison')

def p_comparacion_igual(p):
    '''comparacion : valor IGUAL valor %prec IGUAL'''
    #print('comparacion_igual')
    t1, v1 = p[1]
    t2, v2 = p[3]
    if t1 in ['int', 'float', 'char', 'bool'] and t2 in ['int', 'float', 'char', 'bool']:
        if t1 == t2:
            p[0] = ('bool', v1 == v2)
        elif t1 == 'int' and t2 == 'float' or t1 == 'float' and t2 == 'int':
            p[0] = ('bool', v1 == v2)
        elif t1 == 'char' and t2 == 'int':
            p[0] = ('bool', v1 == v2)
        elif t1 == 'int' and t2 == 'char':
            p[0] = ('bool', v1 == v2)
        elif t1 == 'bool' and t2 == 'bool':
            p[0] = ('bool', v1 == v2)
    else:
        print('[ERROR][PARSER] Type mismatch in comparison')

def p_booleana(p):
    '''booleana : valor CONJUNCION valor %prec CONJUNCION
                | valor DISYUNCION valor %prec DISYUNCION'''
    #print('booleana')
    v1 = p[1]
    v2 = p[3]
    op = p[2]
    #comprobamos en funcion de si están declaradas las variablesd
    if ((type(v1) is tuple) and (type(v2) is tuple)):
        if op == '&&': p[0] = ('bool', bool(v1[1] and v2[1]))
        elif op == '||': p[0] = ('bool', bool(v1[1] or v2[1]))
    elif type(v1) is tuple:
        if op == '&&': p[0] = ('bool', bool(v1[1] and v2))
        elif op == '||': p[0] = ('bool', bool(v1[1] or v2))
    elif type(v2) is tuple:
        if op == '&&': p[0] = ('bool', bool(v1 and v2[1]))
        elif op == '||': p[0] = ('bool', bool(v1 or v2[1]))
    else:
        if op == '&&': p[0] = ('bool', bool(v1 and v2))
        elif op == '||': p[0] = ('bool', bool(v1 or v2))

def p_booleana_negacion(p):
    '''booleana : NEGACION valor %prec NEGACION'''
    #print('booleana_negacion')
    t, v = p[2]
    if t == 'bool':
        p[0] = ('bool', not v)
    else:
        print('[ERROR][PARSER] Type mismatch in negation')

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
    valor = p[3]
    if valor[0] != 'bool':
        print('[ERROR][PARSER] Condition must be a boolean expression')


def p_loop(p):
    '''
    loop : WHILE PARENTESIS_ABRE valor PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA
    '''
    #print('loop')
    valor = p[3]
    if valor[0] != 'bool':
        print('[ERROR][PARSER] Condition must be a boolean expression')



def p_id_t(p):
    '''id_t : variable_t
            | variable_t COMA id_t
            | empty'''
    #print('id_t')
    if len(p) == 2: p[0] = [p[1]]
    elif len(p) == 4: p[0] = [p[1]] + p[3]

def p_variable_t(p):
    '''variable_t : CADENA_NO_COMILLAS DOS_PUNTOS tipo
    '''
    p[0] = (p[3], p[1])

    #print('variable_t')

def p_function_def(p):
    '''
    function_def : FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE id_t PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE statement RETURN valor PUNTO_Y_COMA LLAVE_CIERRA
                 | FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE id_t PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE RETURN valor PUNTO_Y_COMA LLAVE_CIERRA
    '''
    #print('function_def')
    name = p[2]
    tipo = p[7]
    args = p[4]
    arg_t = []
    for arg in args:
        arg_t.append(arg[0])
    name = (name, tuple(arg_t))
    if name in functions:
        print('[ERROR][PARSER] Function %s already defined' % name)
    else:
        functions[name] = (tipo, args)

def p_function_call(p):
    '''
    function_call : CADENA_NO_COMILLAS PARENTESIS_ABRE arg PARENTESIS_CIERRA
    '''
    #print('function_call')
    name = p[1]
    args = p[3]
    aux = []
    for arg in args:
        aux.append(arg[0])
    name = (name, tuple(aux))
    if name in functions:
        tipo, args = functions[name]
        # Hay q hacer que devuelva el resultado????? ##########################################################################################
        p[0] = (tipo, None)
    else:
        print('[ERROR][PARSER] Function %s not defined' % name)

def p_arg(p):
    '''arg : valor
           | valor COMA arg
           | empty'''
    #print('arg')
    if len(p) == 2: p[0] = [p[1]]
    elif len(p) == 4: p[0] = [p[1]] + p[3]
    else: p[0] = []

def p_error(p):
    error = True
    if p: print('[ERROR][PARSER] At line: %s' % p)
    else: print('[ERROR][PARSER] At EOF')

