import ply.yacc as yacc
from Analise_Lexica import *

import Sintaxe_Abstrata as sa
import Visitor as vis


#programa simples
def p_program1(p):
    '''program : comand NEWLINE'''
    if(len (p) == 3)
     p[0] = sa.Program(p[1])


def p_program2(p):
    '''program : function NEWLINE'''
    if(len(p) == 3)
      p[0] = sa.Program(p[1])

def p_program3(p):
    '''program : local_function NEWLINE'''
    if(len(p) == 3)
      p[0] = sa.Program(p[1])

#programa composto
def p_program4(p):
    '''program : comand NEWLINE program'''
    if(len(p) == 4)
      p[0] = sa.Program(p[1],p[3])

def p_program5(p):
    '''program : function NEWLINE program '''
    if(len(p) == 4)
      p[0] = sa.Program(p[1],p[3])

def p_program6(p):
    '''program : local_function NEWLINE program'''
    if(len(p) == 4)
      p[0] = sa.Program(p[1],p[3])

#functions
def p_function(p):
    '''function : FUNCTION signature comands END'''
    if(len(p) == 5)
    p[0] = sa.Function(p[2],p[3])

def p_local_function(p):
    '''local_function : LOCAL FUNCTION signature comands END'''
    if(len(p) == 6)
      p[0] = sa.LocalFunction(p[3],p[4])

#signature
def p_signature1(p):
    '''signature : ID LPAREN sigparams RPAREN'''
    if(len(p) == 5)
      p[0] = sa.Signature(p[1],p[3])

def p_signature2(p):
    '''signature : ID LPAREN RPAREN'''
    if(len(p) == 4)
      p[0] = sa.Signature(p[1])

#sigparams
def p_sigparams(p):
    '''sigparams : ID
                 | ID COMMA sigparams'''
    if(len(p) == 2)
      p[0] = sa.SingleSigparams(p[1])
    else 
      p[0] = sa.CompoundSigparams(p[1],p[3])


#body/comandos
#comands simples
def p_comands1(p):
    '''comands : comand NEWLINE'''
    if(len(p) == 3)
      p[0] = sa.SingleComand(p[1])

#comands composto
def p_comands2(p):
    '''comands : comand NEWLINE comands '''
    if(len(p) == 4)
      p[0] = sa.ComandCompound(p[1], p[3])

#comand
def p_comand1(p):
    '''comand : IF list_exp THEN comands END'''
    if(len(p) == 6)
      p[0] = sa.ComandIf1(p[2],p[4])

def p_comand2(p):
    '''comand : IF list_exp THEN comands ELSE comands END '''
    if(len(p) == 8)
      p[0] = sa.ComandIf2(p[2],p[4],p[6])

def p_comand3(p):
    '''comand : IF list_exp THEN comands elseif ELSE comands END'''
    if(len(p) == 9)
      p[0] = sa.ComandIf3(p[2],p[4],p[5],p[7])

def p_comand4(p):
    '''comand : other_comand'''
    if(len(p) == 3)
      p[0] = sa.ComandOtherComand(p[1])

#elseif
def p_elseif1(p):
    '''elseif : ELSEIF list_exp THEN comands'''
    p[0] = sa.SingleElseIf(p[2],p[4])

def p_elseif2(p):
    '''elseif : ELSEIF list_exp THEN comands elseif'''
    p[0] = sa.CompoundElseIf(p[2],p[4],p[5])

#other_comand
def p_other_comand1(p):
    '''other_comand : WHILE list_exp DO comands END'''


def p_other_comand2(p):
    '''other_comand : fordo'''


def p_other_comand3(p):
    '''other_comand : exp'''


def p_other_comand4(p):
    '''other_comand : forin'''


def p_other_comand5(p):
    '''other_comand : RETURN exp'''


def p_other_comand6(p):
    '''other_comand : BREAK'''


def p_fordo(p):
    '''fordo : FOR list_exp DO comands END'''


def p_forin(p):
    '''forin : FOR list_exp IN exp DO comands END'''


#uma "lista de expressões entre parenteses ou ela sozinha"
def p_list_exp(p):
    '''list_exp : LPAREN exp RPAREN 
              | exp'''


#chamada de função
def p_call(p):
    '''call : ID LPAREN exp RPAREN
          | ID LPAREN RPAREN'''


#array
def p_array(p):
    '''array : LKEY exp RKEY
           | LKEY RKEY
           | ID LCOCHETE exp RCOCHETE
           | ID LCOCHETE RCOCHETE'''


#expressões
def p_exp(p):
    '''exp : exp ASSIGN exp_1
           | exp_1'''


def p_exp_1(p):
    '''exp_1 : exp_1 OR exp_2
           | exp_2'''


def p_exp_2(p):
    '''exp_2 : exp_2 AND exp_3
           | exp_3'''


def p_exp_3(p):
    '''exp_3 : exp_3 LESS_THAN exp_4
           | exp_4'''


def p_exp_4(p):
    '''exp_4 : exp_4 BIGGER_THAN exp_5
           | exp_5'''


def p_exp_5(p):
    '''exp_5 : exp_5 LESS_EQUAL exp_6
           | exp_6'''


def p_exp_6(p):
    '''exp_6 : exp_6 BIGGER_EQUAL exp_7
           | exp_7'''


def p_exp_7(p):
    '''exp_7 : exp_7 DIF exp_8
           | exp_8'''


def p_exp_8(p):
    '''exp_8 : exp_8 EQUAL exp_9
           | exp_9'''


def p_exp_9(p):
    '''exp_9 : exp_9 BITWISE_OR exp_10
           | exp_10'''


def p_exp_10(p):
    '''exp_10 : exp_10 BITWISE_EXC_OR exp_11
            | exp_11'''


def p_exp_11(p):
    '''exp_11 : exp_11 BITWISE_AND exp_12
            | exp_12'''


def p_exp_12(p):
    '''exp_12 : exp_12 CONCATENATION exp_13
           | exp_13'''


def p_exp_13(p):
    '''exp_13 : exp_13 SUB exp_14
           | exp_14'''


def p_exp_14(p):
    '''exp_14 : exp_14 SUM exp_15
           | exp_15'''


def p_exp_15(p):
    '''exp_15 : exp_15 MODULE exp_16
           | exp_16'''


def p_exp_16(p):
    '''exp_16 : exp_16 DIV_INT exp_17
            | exp_17'''


def p_exp_17(p):
    '''exp_17 : exp_17 DIV exp_18
            | exp_18'''


def p_exp_18(p):
    '''exp_18 : exp_18 MULT exp_19
            | exp_19'''


def p_exp_19(p):
    '''exp_19 : exp_19 NOT exp_20
            | exp_20'''


def p_exp_20(p):
    '''exp_20 : DENIAL exp_20
            | exp_21'''


def p_exp_21(p):
    '''exp_21 : UNARY_BITWISE_NOT exp_21
            | exp_22'''


def p_exp_22(p):
    '''exp_22 : LENGHT exp_22
            | exp_23'''


def p_exp_23(p):
    '''exp_23 : exp_23 POW exp_24
            | exp_24'''


def p_exp_24(p): 
    '''exp_24 : exp_24 COMMA exp_25
            | exp_24 DOT exp_25
            | array
            | call
            | exp_25'''


def p_exp_25(p):
    '''exp_25 : NUMBER 
            | STRING 
            | LOCAL ID
            | ID
            | NIL
            | TRUE
            | FALSE'''


def p_error(p):
    print("Erro Sintático")
