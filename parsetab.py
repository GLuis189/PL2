
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSUMARESTAleftMULTIPLICACIONDIVISIONrightUPLUSUMINUSleftCONJUNCIONDISYUNCIONrightNEGACIONnonassocMENOR_IGUALMENORMAYOR_IGUALMAYORIGUALASIGNACION BOOLEAN CADENA_COMILLAS CADENA_NO_COMILLAS CARACTER CHARACTER COMA CONJUNCION CORCHETE_ABRE CORCHETE_CIERRA DECIMAL DISYUNCION DIVISION DOS_PUNTOS ELSE ENTERO FL FLOAT FUNCTION IF IGUAL INT LET LLAVE_ABRE LLAVE_CIERRA MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MULTIPLICACION NEGACION NULL PARENTESIS_ABRE PARENTESIS_CIERRA PUNTO PUNTO_Y_COMA RESTA RETURN SUMA TR TYPE WHILEprograma : statement\n                | emptyempty : \n    statement : content PUNTO_Y_COMA\n              | content PUNTO_Y_COMA statement\n              | no_semicolon\n              | no_semicolon statement\n    \n    content : define\n            | declare\n            | assign\n    \n    no_semicolon : condition\n                 | loop\n                 | function_def\n    ident : CADENA_NO_COMILLAS\n             | CADENA_NO_COMILLAS PUNTO ident\n             | CADENA_NO_COMILLAS CORCHETE_ABRE CADENA_COMILLAS CORCHETE_CIERRA\n             | CADENA_NO_COMILLAS CORCHETE_ABRE CADENA_COMILLAS CORCHETE_CIERRA PUNTO ident\n             \n    declare : LET id\n    id : variable\n          | variable COMA id\n          | variable ASIGNACION valor\n          | variable ASIGNACION valor COMA idvariable : ident\n                | ident DOS_PUNTOS tipo\n    assign : variable ASIGNACION valor\n    valor : ident\n             | ENTERO\n             | DECIMAL\n             | operacion\n             | TR\n             | FL\n             | NULL\n             | ajson_v\n             | CARACTER\n             | function_call\n             | PARENTESIS_ABRE valor PARENTESIS_CIERRA\n             | SUMA valor %prec UPLUS\n             | RESTA valor %prec UMINUS\n    \n    define : TYPE CADENA_NO_COMILLAS ASIGNACION ajson\n    ajson : LLAVE_ABRE lista LLAVE_CIERRAlista : elemento\n             | elemento COMA \n             | elemento COMA listaelemento : clave DOS_PUNTOS valor_tvalor_t : tipo\n               | ajsonclave : CADENA_NO_COMILLAS\n             | CADENA_COMILLASajson_v : LLAVE_ABRE lista_v LLAVE_CIERRAlista_v : elemento_v\n               | elemento_v COMA \n               | elemento_v COMA lista_velemento_v : clave_v DOS_PUNTOS valorclave_v : CADENA_NO_COMILLAS\n               | CADENA_COMILLASoperacion : aritmetica\n                 | booleana\n                 | comparacionaritmetica : valor SUMA valor\n                  | valor RESTA valor\n                  | valor MULTIPLICACION valor\n                  | valor DIVISION valorcomparacion : valor MAYOR valor\n                   | valor MENOR valor\n                   | valor MAYOR_IGUAL valor\n                   | valor MENOR_IGUAL valor\n                   | valor IGUAL valorbooleana : valor CONJUNCION valor\n                | valor DISYUNCION valor\n                | NEGACION valortipo : INT\n            | FLOAT\n            | CHARACTER\n            | BOOLEAN\n            | CADENA_NO_COMILLAS\n    \n    condition : IF PARENTESIS_ABRE valor PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA\n              | IF PARENTESIS_ABRE valor PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA ELSE LLAVE_ABRE statement LLAVE_CIERRA\n    \n    loop : WHILE PARENTESIS_ABRE valor PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA\n    \n    function_def : FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE id PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE statement RETURN valor PUNTO_Y_COMA LLAVE_CIERRA\n                 | FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE id PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE RETURN valor PUNTO_Y_COMA LLAVE_CIERRA\n                 | FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE statement RETURN valor PUNTO_Y_COMA LLAVE_CIERRA\n                 | FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE RETURN valor PUNTO_Y_COMA LLAVE_CIERRA\n    \n    function_call : CADENA_NO_COMILLAS PARENTESIS_ABRE arg PARENTESIS_CIERRA\n                  | CADENA_NO_COMILLAS PARENTESIS_ABRE PARENTESIS_CIERRA\n    arg : valor\n           | valor COMA arg'
    
_lr_action_items = {'$end':([0,1,2,3,5,9,10,11,20,21,32,144,145,162,166,168,169,170,],[-3,0,-1,-2,-6,-11,-12,-13,-4,-7,-5,-76,-78,-77,-82,-80,-81,-79,]),'TYPE':([0,5,9,10,11,20,122,123,144,145,147,149,152,162,166,168,169,170,],[12,12,-11,-12,-13,12,12,12,-76,-78,12,12,12,-77,-82,-80,-81,-79,]),'LET':([0,5,9,10,11,20,122,123,144,145,147,149,152,162,166,168,169,170,],[14,14,-11,-12,-13,14,14,14,-76,-78,14,14,14,-77,-82,-80,-81,-79,]),'IF':([0,5,9,10,11,20,122,123,144,145,147,149,152,162,166,168,169,170,],[16,16,-11,-12,-13,16,16,16,-76,-78,16,16,16,-77,-82,-80,-81,-79,]),'WHILE':([0,5,9,10,11,20,122,123,144,145,147,149,152,162,166,168,169,170,],[17,17,-11,-12,-13,17,17,17,-76,-78,17,17,17,-77,-82,-80,-81,-79,]),'FUNCTION':([0,5,9,10,11,20,122,123,144,145,147,149,152,162,166,168,169,170,],[18,18,-11,-12,-13,18,18,18,-76,-78,18,18,18,-77,-82,-80,-81,-79,]),'CADENA_NO_COMILLAS':([0,5,9,10,11,12,14,18,20,23,27,28,29,31,36,37,49,50,51,56,57,60,68,72,73,74,75,76,77,78,79,80,81,82,86,102,103,120,121,122,123,125,127,128,132,137,144,145,147,149,151,152,154,155,158,162,166,168,169,170,],[13,13,-11,-12,-13,22,13,30,13,13,52,52,52,66,13,52,52,52,52,90,52,13,100,52,52,52,52,52,52,52,52,52,52,52,52,13,13,90,52,13,13,66,100,66,52,66,-76,-78,13,13,52,13,52,52,52,-77,-82,-80,-81,-79,]),'PUNTO_Y_COMA':([4,6,7,8,13,19,25,26,34,38,39,40,41,42,43,44,45,46,47,48,52,53,54,55,61,62,63,64,65,66,67,69,70,71,84,85,92,104,105,106,107,108,109,110,111,112,113,114,115,117,119,126,129,130,131,156,159,160,163,],[20,-8,-9,-10,-14,-23,-18,-19,-15,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-14,-56,-57,-58,-24,-71,-72,-73,-74,-75,-39,-16,-20,-21,-37,-38,-70,-59,-60,-61,-62,-68,-69,-63,-64,-65,-66,-67,-36,-84,-49,-40,-17,-22,-83,161,164,165,167,]),'LLAVE_CIERRA':([5,9,10,11,13,20,21,32,34,39,40,41,42,43,44,45,46,47,48,52,53,54,55,62,63,64,65,66,69,84,85,87,88,92,97,98,104,105,106,107,108,109,110,111,112,113,114,115,117,119,120,126,127,129,131,133,134,135,136,139,140,141,142,144,145,157,161,162,164,165,166,167,168,169,170,],[-6,-11,-12,-13,-14,-4,-7,-5,-15,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-14,-56,-57,-58,-71,-72,-73,-74,-75,-16,-37,-38,119,-50,-70,126,-41,-59,-60,-61,-62,-68,-69,-63,-64,-65,-66,-67,-36,-84,-49,-51,-40,-42,-17,-83,-52,-53,144,145,-43,-44,-45,-46,-76,-78,162,166,-77,168,169,-82,170,-80,-81,-79,]),'RETURN':([5,9,10,11,20,21,32,144,145,147,149,150,153,162,166,168,169,170,],[-6,-11,-12,-13,-4,-7,-5,-76,-78,151,154,155,158,-77,-82,-80,-81,-79,]),'DOS_PUNTOS':([13,19,34,69,89,90,91,96,99,100,101,124,129,],[-14,31,-15,-16,121,-54,-55,125,128,-47,-48,137,-17,]),'ASIGNACION':([13,15,19,22,26,34,61,62,63,64,65,66,69,129,],[-14,27,-23,33,37,-15,-24,-71,-72,-73,-74,-75,-16,-17,]),'COMA':([13,19,26,34,39,40,41,42,43,44,45,46,47,48,52,53,54,55,61,62,63,64,65,66,69,71,84,85,88,92,98,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,126,129,131,134,140,141,142,],[-14,-23,36,-15,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-14,-56,-57,-58,-24,-71,-72,-73,-74,-75,-16,103,-37,-38,120,-70,127,-59,-60,-61,-62,-68,-69,-63,-64,-65,-66,-67,-36,-84,132,-49,-40,-17,-83,-53,-44,-45,-46,]),'SUMA':([13,27,28,29,34,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,59,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,92,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,121,129,131,132,134,151,154,155,156,158,159,160,163,],[-14,50,50,50,-15,50,72,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,50,50,50,-14,-56,-57,-58,50,72,72,-16,72,50,50,50,50,50,50,50,50,50,50,50,72,-37,-38,50,-70,-59,-60,-61,-62,-68,-69,-63,-64,-65,-66,-67,-36,-84,72,-49,50,-17,-83,50,72,50,50,50,72,50,72,72,72,]),'RESTA':([13,27,28,29,34,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,59,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,92,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,121,129,131,132,134,151,154,155,156,158,159,160,163,],[-14,51,51,51,-15,51,73,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,51,51,51,-14,-56,-57,-58,51,73,73,-16,73,51,51,51,51,51,51,51,51,51,51,51,73,-37,-38,51,-70,-59,-60,-61,-62,-68,-69,-63,-64,-65,-66,-67,-36,-84,73,-49,51,-17,-83,51,73,51,51,51,73,51,73,73,73,]),'MULTIPLICACION':([13,34,38,39,40,41,42,43,44,45,46,47,48,52,53,54,55,58,59,69,71,83,84,85,92,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,129,131,134,156,159,160,163,],[-14,-15,74,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-14,-56,-57,-58,74,74,-16,74,74,-37,-38,-70,74,74,-61,-62,-68,-69,-63,-64,-65,-66,-67,-36,-84,74,-49,-17,-83,74,74,74,74,74,]),'DIVISION':([13,34,38,39,40,41,42,43,44,45,46,47,48,52,53,54,55,58,59,69,71,83,84,85,92,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,129,131,134,156,159,160,163,],[-14,-15,75,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-14,-56,-57,-58,75,75,-16,75,75,-37,-38,-70,75,75,-61,-62,-68,-69,-63,-64,-65,-66,-67,-36,-84,75,-49,-17,-83,75,75,75,75,75,]),'CONJUNCION':([13,34,38,39,40,41,42,43,44,45,46,47,48,52,53,54,55,58,59,69,71,83,84,85,92,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,129,131,134,156,159,160,163,],[-14,-15,76,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-14,-56,-57,-58,76,76,-16,76,76,76,76,-70,76,76,76,76,-68,-69,-63,-64,-65,-66,-67,-36,-84,76,-49,-17,-83,76,76,76,76,76,]),'DISYUNCION':([13,34,38,39,40,41,42,43,44,45,46,47,48,52,53,54,55,58,59,69,71,83,84,85,92,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,129,131,134,156,159,160,163,],[-14,-15,77,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-14,-56,-57,-58,77,77,-16,77,77,77,77,-70,77,77,77,77,-68,-69,-63,-64,-65,-66,-67,-36,-84,77,-49,-17,-83,77,77,77,77,77,]),'MAYOR':([13,34,38,39,40,41,42,43,44,45,46,47,48,52,53,54,55,58,59,69,71,83,84,85,92,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,129,131,134,156,159,160,163,],[-14,-15,78,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-14,-56,-57,-58,78,78,-16,78,78,78,78,78,78,78,78,78,78,78,None,None,None,None,None,-36,-84,78,-49,-17,-83,78,78,78,78,78,]),'MENOR':([13,34,38,39,40,41,42,43,44,45,46,47,48,52,53,54,55,58,59,69,71,83,84,85,92,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,129,131,134,156,159,160,163,],[-14,-15,79,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-14,-56,-57,-58,79,79,-16,79,79,79,79,79,79,79,79,79,79,79,None,None,None,None,None,-36,-84,79,-49,-17,-83,79,79,79,79,79,]),'MAYOR_IGUAL':([13,34,38,39,40,41,42,43,44,45,46,47,48,52,53,54,55,58,59,69,71,83,84,85,92,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,129,131,134,156,159,160,163,],[-14,-15,80,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-14,-56,-57,-58,80,80,-16,80,80,80,80,80,80,80,80,80,80,80,None,None,None,None,None,-36,-84,80,-49,-17,-83,80,80,80,80,80,]),'MENOR_IGUAL':([13,34,38,39,40,41,42,43,44,45,46,47,48,52,53,54,55,58,59,69,71,83,84,85,92,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,129,131,134,156,159,160,163,],[-14,-15,81,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-14,-56,-57,-58,81,81,-16,81,81,81,81,81,81,81,81,81,81,81,None,None,None,None,None,-36,-84,81,-49,-17,-83,81,81,81,81,81,]),'IGUAL':([13,34,38,39,40,41,42,43,44,45,46,47,48,52,53,54,55,58,59,69,71,83,84,85,92,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,129,131,134,156,159,160,163,],[-14,-15,82,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-14,-56,-57,-58,82,82,-16,82,82,82,82,82,82,82,82,82,82,82,None,None,None,None,None,-36,-84,82,-49,-17,-83,82,82,82,82,82,]),'PARENTESIS_CIERRA':([13,19,26,34,39,40,41,42,43,44,45,46,47,48,52,53,54,55,58,59,60,61,62,63,64,65,66,69,70,71,83,84,85,86,92,95,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,129,130,131,143,],[-14,-23,-19,-15,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-14,-56,-57,-58,93,94,96,-24,-71,-72,-73,-74,-75,-16,-20,-21,115,-37,-38,117,-70,124,-59,-60,-61,-62,-68,-69,-63,-64,-65,-66,-67,-36,131,-84,-85,-49,-17,-22,-83,-86,]),'PUNTO':([13,52,69,],[23,23,102,]),'CORCHETE_ABRE':([13,52,],[24,24,]),'PARENTESIS_ABRE':([16,17,27,28,29,30,37,49,50,51,52,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[28,29,49,49,49,60,49,49,49,49,86,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'CADENA_COMILLAS':([24,56,68,120,127,],[35,91,101,91,101,]),'ENTERO':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'DECIMAL':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'TR':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'FL':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'NULL':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'CARACTER':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'LLAVE_ABRE':([27,28,29,33,37,49,50,51,57,62,63,64,65,66,72,73,74,75,76,77,78,79,80,81,82,86,93,94,121,128,132,138,146,148,151,154,155,158,],[56,56,56,68,56,56,56,56,56,-71,-72,-73,-74,-75,56,56,56,56,56,56,56,56,56,56,56,56,122,123,56,68,56,147,149,152,56,56,56,56,]),'NEGACION':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'INT':([31,125,128,137,],[62,62,62,62,]),'FLOAT':([31,125,128,137,],[63,63,63,63,]),'CHARACTER':([31,125,128,137,],[64,64,64,64,]),'BOOLEAN':([31,125,128,137,],[65,65,65,65,]),'CORCHETE_CIERRA':([35,],[69,]),'ELSE':([144,],[148,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'statement':([0,5,20,122,123,147,149,152,],[2,21,32,135,136,150,153,157,]),'empty':([0,],[3,]),'content':([0,5,20,122,123,147,149,152,],[4,4,4,4,4,4,4,4,]),'no_semicolon':([0,5,20,122,123,147,149,152,],[5,5,5,5,5,5,5,5,]),'define':([0,5,20,122,123,147,149,152,],[6,6,6,6,6,6,6,6,]),'declare':([0,5,20,122,123,147,149,152,],[7,7,7,7,7,7,7,7,]),'assign':([0,5,20,122,123,147,149,152,],[8,8,8,8,8,8,8,8,]),'condition':([0,5,20,122,123,147,149,152,],[9,9,9,9,9,9,9,9,]),'loop':([0,5,20,122,123,147,149,152,],[10,10,10,10,10,10,10,10,]),'function_def':([0,5,20,122,123,147,149,152,],[11,11,11,11,11,11,11,11,]),'variable':([0,5,14,20,36,60,103,122,123,147,149,152,],[15,15,26,15,26,26,26,15,15,15,15,15,]),'ident':([0,5,14,20,23,27,28,29,36,37,49,50,51,57,60,72,73,74,75,76,77,78,79,80,81,82,86,102,103,121,122,123,132,147,149,151,152,154,155,158,],[19,19,19,19,34,39,39,39,19,39,39,39,39,39,19,39,39,39,39,39,39,39,39,39,39,39,39,129,19,39,19,19,39,19,19,39,19,39,39,39,]),'id':([14,36,60,103,],[25,70,95,130,]),'valor':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[38,58,59,71,83,84,85,92,104,105,106,107,108,109,110,111,112,113,114,118,134,118,156,159,160,163,]),'operacion':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'ajson_v':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'function_call':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'aritmetica':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'booleana':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'comparacion':([27,28,29,37,49,50,51,57,72,73,74,75,76,77,78,79,80,81,82,86,121,132,151,154,155,158,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'tipo':([31,125,128,137,],[61,138,141,146,]),'ajson':([33,128,],[67,142,]),'lista_v':([56,120,],[87,133,]),'elemento_v':([56,120,],[88,88,]),'clave_v':([56,120,],[89,89,]),'lista':([68,127,],[97,139,]),'elemento':([68,127,],[98,98,]),'clave':([68,127,],[99,99,]),'arg':([86,132,],[116,143,]),'valor_t':([128,],[140,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> statement','programa',1,'p_programa','parser_ajs.py',16),
  ('programa -> empty','programa',1,'p_programa','parser_ajs.py',17),
  ('empty -> <empty>','empty',0,'p_empty','parser_ajs.py',21),
  ('statement -> content PUNTO_Y_COMA','statement',2,'p_statement','parser_ajs.py',26),
  ('statement -> content PUNTO_Y_COMA statement','statement',3,'p_statement','parser_ajs.py',27),
  ('statement -> no_semicolon','statement',1,'p_statement','parser_ajs.py',28),
  ('statement -> no_semicolon statement','statement',2,'p_statement','parser_ajs.py',29),
  ('content -> define','content',1,'p_content','parser_ajs.py',35),
  ('content -> declare','content',1,'p_content','parser_ajs.py',36),
  ('content -> assign','content',1,'p_content','parser_ajs.py',37),
  ('no_semicolon -> condition','no_semicolon',1,'p_no_semicolon','parser_ajs.py',43),
  ('no_semicolon -> loop','no_semicolon',1,'p_no_semicolon','parser_ajs.py',44),
  ('no_semicolon -> function_def','no_semicolon',1,'p_no_semicolon','parser_ajs.py',45),
  ('ident -> CADENA_NO_COMILLAS','ident',1,'p_ident','parser_ajs.py',50),
  ('ident -> CADENA_NO_COMILLAS PUNTO ident','ident',3,'p_ident','parser_ajs.py',51),
  ('ident -> CADENA_NO_COMILLAS CORCHETE_ABRE CADENA_COMILLAS CORCHETE_CIERRA','ident',4,'p_ident','parser_ajs.py',52),
  ('ident -> CADENA_NO_COMILLAS CORCHETE_ABRE CADENA_COMILLAS CORCHETE_CIERRA PUNTO ident','ident',6,'p_ident','parser_ajs.py',53),
  ('declare -> LET id','declare',2,'p_declare','parser_ajs.py',61),
  ('id -> variable','id',1,'p_id','parser_ajs.py',66),
  ('id -> variable COMA id','id',3,'p_id','parser_ajs.py',67),
  ('id -> variable ASIGNACION valor','id',3,'p_id','parser_ajs.py',68),
  ('id -> variable ASIGNACION valor COMA id','id',5,'p_id','parser_ajs.py',69),
  ('variable -> ident','variable',1,'p_variable','parser_ajs.py',73),
  ('variable -> ident DOS_PUNTOS tipo','variable',3,'p_variable','parser_ajs.py',74),
  ('assign -> variable ASIGNACION valor','assign',3,'p_assign','parser_ajs.py',81),
  ('valor -> ident','valor',1,'p_valor','parser_ajs.py',86),
  ('valor -> ENTERO','valor',1,'p_valor','parser_ajs.py',87),
  ('valor -> DECIMAL','valor',1,'p_valor','parser_ajs.py',88),
  ('valor -> operacion','valor',1,'p_valor','parser_ajs.py',89),
  ('valor -> TR','valor',1,'p_valor','parser_ajs.py',90),
  ('valor -> FL','valor',1,'p_valor','parser_ajs.py',91),
  ('valor -> NULL','valor',1,'p_valor','parser_ajs.py',92),
  ('valor -> ajson_v','valor',1,'p_valor','parser_ajs.py',93),
  ('valor -> CARACTER','valor',1,'p_valor','parser_ajs.py',94),
  ('valor -> function_call','valor',1,'p_valor','parser_ajs.py',95),
  ('valor -> PARENTESIS_ABRE valor PARENTESIS_CIERRA','valor',3,'p_valor','parser_ajs.py',96),
  ('valor -> SUMA valor','valor',2,'p_valor','parser_ajs.py',97),
  ('valor -> RESTA valor','valor',2,'p_valor','parser_ajs.py',98),
  ('define -> TYPE CADENA_NO_COMILLAS ASIGNACION ajson','define',4,'p_define','parser_ajs.py',105),
  ('ajson -> LLAVE_ABRE lista LLAVE_CIERRA','ajson',3,'p_ajson','parser_ajs.py',110),
  ('lista -> elemento','lista',1,'p_lista','parser_ajs.py',114),
  ('lista -> elemento COMA','lista',2,'p_lista','parser_ajs.py',115),
  ('lista -> elemento COMA lista','lista',3,'p_lista','parser_ajs.py',116),
  ('elemento -> clave DOS_PUNTOS valor_t','elemento',3,'p_elemento','parser_ajs.py',120),
  ('valor_t -> tipo','valor_t',1,'p_valor_t','parser_ajs.py',124),
  ('valor_t -> ajson','valor_t',1,'p_valor_t','parser_ajs.py',125),
  ('clave -> CADENA_NO_COMILLAS','clave',1,'p_clave','parser_ajs.py',129),
  ('clave -> CADENA_COMILLAS','clave',1,'p_clave','parser_ajs.py',130),
  ('ajson_v -> LLAVE_ABRE lista_v LLAVE_CIERRA','ajson_v',3,'p_ajson_v','parser_ajs.py',134),
  ('lista_v -> elemento_v','lista_v',1,'p_lista_v','parser_ajs.py',138),
  ('lista_v -> elemento_v COMA','lista_v',2,'p_lista_v','parser_ajs.py',139),
  ('lista_v -> elemento_v COMA lista_v','lista_v',3,'p_lista_v','parser_ajs.py',140),
  ('elemento_v -> clave_v DOS_PUNTOS valor','elemento_v',3,'p_elemento_v','parser_ajs.py',144),
  ('clave_v -> CADENA_NO_COMILLAS','clave_v',1,'p_clave_v','parser_ajs.py',148),
  ('clave_v -> CADENA_COMILLAS','clave_v',1,'p_clave_v','parser_ajs.py',149),
  ('operacion -> aritmetica','operacion',1,'p_operacion','parser_ajs.py',153),
  ('operacion -> booleana','operacion',1,'p_operacion','parser_ajs.py',154),
  ('operacion -> comparacion','operacion',1,'p_operacion','parser_ajs.py',155),
  ('aritmetica -> valor SUMA valor','aritmetica',3,'p_aritmetica','parser_ajs.py',160),
  ('aritmetica -> valor RESTA valor','aritmetica',3,'p_aritmetica','parser_ajs.py',161),
  ('aritmetica -> valor MULTIPLICACION valor','aritmetica',3,'p_aritmetica','parser_ajs.py',162),
  ('aritmetica -> valor DIVISION valor','aritmetica',3,'p_aritmetica','parser_ajs.py',163),
  ('comparacion -> valor MAYOR valor','comparacion',3,'p_comparacion','parser_ajs.py',177),
  ('comparacion -> valor MENOR valor','comparacion',3,'p_comparacion','parser_ajs.py',178),
  ('comparacion -> valor MAYOR_IGUAL valor','comparacion',3,'p_comparacion','parser_ajs.py',179),
  ('comparacion -> valor MENOR_IGUAL valor','comparacion',3,'p_comparacion','parser_ajs.py',180),
  ('comparacion -> valor IGUAL valor','comparacion',3,'p_comparacion','parser_ajs.py',181),
  ('booleana -> valor CONJUNCION valor','booleana',3,'p_booleana','parser_ajs.py',193),
  ('booleana -> valor DISYUNCION valor','booleana',3,'p_booleana','parser_ajs.py',194),
  ('booleana -> NEGACION valor','booleana',2,'p_booleana','parser_ajs.py',195),
  ('tipo -> INT','tipo',1,'p_tipo','parser_ajs.py',206),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser_ajs.py',207),
  ('tipo -> CHARACTER','tipo',1,'p_tipo','parser_ajs.py',208),
  ('tipo -> BOOLEAN','tipo',1,'p_tipo','parser_ajs.py',209),
  ('tipo -> CADENA_NO_COMILLAS','tipo',1,'p_tipo','parser_ajs.py',210),
  ('condition -> IF PARENTESIS_ABRE valor PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA','condition',7,'p_condition','parser_ajs.py',216),
  ('condition -> IF PARENTESIS_ABRE valor PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA ELSE LLAVE_ABRE statement LLAVE_CIERRA','condition',11,'p_condition','parser_ajs.py',217),
  ('loop -> WHILE PARENTESIS_ABRE valor PARENTESIS_CIERRA LLAVE_ABRE statement LLAVE_CIERRA','loop',7,'p_loop','parser_ajs.py',223),
  ('function_def -> FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE id PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE statement RETURN valor PUNTO_Y_COMA LLAVE_CIERRA','function_def',13,'p_function_def','parser_ajs.py',229),
  ('function_def -> FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE id PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE RETURN valor PUNTO_Y_COMA LLAVE_CIERRA','function_def',12,'p_function_def','parser_ajs.py',230),
  ('function_def -> FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE statement RETURN valor PUNTO_Y_COMA LLAVE_CIERRA','function_def',12,'p_function_def','parser_ajs.py',231),
  ('function_def -> FUNCTION CADENA_NO_COMILLAS PARENTESIS_ABRE PARENTESIS_CIERRA DOS_PUNTOS tipo LLAVE_ABRE RETURN valor PUNTO_Y_COMA LLAVE_CIERRA','function_def',11,'p_function_def','parser_ajs.py',232),
  ('function_call -> CADENA_NO_COMILLAS PARENTESIS_ABRE arg PARENTESIS_CIERRA','function_call',4,'p_function_call','parser_ajs.py',238),
  ('function_call -> CADENA_NO_COMILLAS PARENTESIS_ABRE PARENTESIS_CIERRA','function_call',3,'p_function_call','parser_ajs.py',239),
  ('arg -> valor','arg',1,'p_arg','parser_ajs.py',244),
  ('arg -> valor COMA arg','arg',3,'p_arg','parser_ajs.py',245),
]
