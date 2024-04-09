import ply.lex as lex
from tokens import Tokens

tokens = Tokens.tokens + Tokens.reserved

reserved_map = { }
for r in Tokens.reserved:
    reserved_map[r.lower()] = r

t_LLAVE_ABRE = r"\{"
t_LLAVE_CIERRA = r"\}"
t_COMA = r","
t_DOS_PUNTOS = r":"
t_IGUAL = r"=="
t_MAYOR = r">"
t_MENOR = r"<"
t_MAYOR_IGUAL = r">="
t_MENOR_IGUAL = r"<="
t_CORCHETE_ABRE = r"\["
t_CORCHETE_CIERRA = r"\]"
t_PUNTO_Y_COMA = r";"
t_PUNTO = r"\."
t_PARENTESIS_ABRE = r"\("
t_PARENTESIS_CIERRA = r"\)"
t_COMENTARIO_LINEA = r"//.*"
t_COMENTARIO_BLOQUE = r"/\*.*\*/"
t_CONJUNCION = r"&&"
t_DISYUNCION = r"\|\|"
t_NEGACION = r"!"
t_SUMA = r"\+"
t_RESTA = r"-"
t_MULTIPLICACION = r"\*"
t_DIVISION = r"/"
t_ASIGNACION = r"="

def t_COMENTARIO_LINEA(t):
    r"//.*"
    pass

def t_COMENTARIO_BLOQUE(t):
    r"/\*.*\*/"
    t.lexer.lineno += t.value.count("\n")
    pass

def t_CADENA_NO_COMILLAS(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved_map.get(t.value, "CADENA_NO_COMILLAS")
    if t.type == "TR":
        t.value = True
    elif t.type == "FL":
        t.value = False
    elif t.type == "NULL":
        t.value = None
    return t

def t_CADENA_COMILLAS(t):
    r"\"[^\"]*\""
    t.value = t.value[1:-1]
    return t

def t_CARACTER(t):
    r"'.'"
    t.value = t.value[1]
    return t

entero = r"-?\d+"
decimal = r"-?(\d+\.\d+)|(\.\d+)"
cientifico = r"-?((\d+\.\d+)|(\.\d+)|(\d+))[eE]-?\d+"
binario = r"0(b|B)[01]+"
octal = r"0[0-7]+"
hexadecimal = r"0(x|X)[0-9a-fA-F]+"
numero = r"|".join([ binario, hexadecimal, cientifico, decimal, entero, octal])

@lex.TOKEN(numero)
def t_NUMERO(t):
    if t.value.startswith("0b") or t.value.startswith("0B"):
        t.value = int(t.value, 2)
    elif t.value.startswith("0x") or t.value.startswith("0X"):
        t.value = int(t.value, 16)
    elif t.value.startswith("0") and all(c in '01234567' for c in t.value[1:]):
        t.value = int(t.value, 8)
    elif "." in t.value or "e" in t.value or "E" in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)