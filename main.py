import sys
import lexer_ajs
import parser_ajs
import ply.lex as lex
import ply.yacc as yacc

file_name = sys.argv[1]
file = open(file_name, 'r')
content = file.read()

if len(sys.argv) < 3:
    lexer_ajs = lex.lex(module=lexer_ajs)
    lexer_ajs.input(content)
    for token in lexer_ajs:
        print(token.type, token.value)
    parser = yacc.yacc(module=parser_ajs)
    result = parser.parse(content, lexer=lexer_ajs)
elif sys.argv[2] and sys.argv[2] == '-lex':
    lexer_ajs = lex.lex(module=lexer_ajs)
    lexer_ajs.input(content)
    for token in lexer_ajs:
        print(token.type, token.value)

elif sys.argv[2] and sys.argv[2] == '-par':
    lexer_ajs = lex.lex(module=lexer_ajs)
    lexer_ajs.input(content)
    parser = yacc.yacc(module=parser_ajs)
    result = parser.parse(content, lexer=lexer_ajs)
else:
    print("Invalid command")
    