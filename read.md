
#Precedência dos Operadores

#1º  ^
#2º  not,  #,  – (unário)
#3º  *,  /,  %
#4º  +,  –
#5º  ..
#6º  >,  >=,  <,  <=, ==, ~=
#7º  and
#8º   or

#A precedência de operadores em Lua, do maior para o menor:

#parênteses: (, )
#exponenciação: ^
#operadores unários: not, #, -, ~
#multiplicação: *
#divisão: /
#divisão inteira: //
#módulo: %
#adição: +
#subtração: -
#concatenação de string: ..
#operadores bit a bit: <<, >>, &, ~, |
#operadores repcionais: <, >, <=, >=, ~=, ==
#operadores lógicos: and, or
  
#Obs: Para os operadores de mesma precêdencia eles são associativos a esquerda com a excessão do ^ e do .. que são a direita.