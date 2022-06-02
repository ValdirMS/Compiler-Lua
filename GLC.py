#1-https://www.luiztools.com.br/post/introducao-a-linguagem-de-programacao-lua/
#2-https://lplua.wordpress.com/sintaxe/operadores/
#3-https://www.lua.org/manual/5.1/pt/manual.html
#4-https://github.com/andreluisms/TutorialSemantico02/blob/main/glc
#5-https://www.lua.org/pil/contents.html
#6-https://www.lua.org/pil/4.3.1.html


#SEMICOLON, COLON, COMMENT

program → comands
        |function
        |comands program
        |function program

  
#talvez precise mudar o "comands" para "body" aqui  
function → FUNCTION signature comands END 
           |LOCAL FUNCTION signature comands END

signature → ID "(" sigparam ")"

sigparam → ID
           |ID "," sigparam

comands → comand
          |comand comands
# comands representa o body
comand →  comand_1
         |comand_1 END
         |comand_2
         |comand_2 END

comand_1 -> IF list_exp THEN if_body 
            |ELSEIF list_exp THEN if_body
            |other_comand    

other_comand -> WHILE list_exp DO comands  
            |fordo_forin
            | exp
            | RETURN
            | BREAK 

  
if_body → comand_1 ELSE comand_1|
          comands ELSE comands|
          comand_1 ELSE comands|
          comands ELSE comand_1|
  
comand_2-> IF list_exp THEN comands 
           | IF list_exp THEN comand_1 ELSE comand_2 
           | IF list_exp THEN comands ELSE comand_2 


fordo_forin → FOR list_exp DO comands |
              FOR list_exp IN list_exp comands
              
        
list_exp → exp "," list_exp 
         |exp
         |exp list_exp
         |paren_list_exp list_exp
  

paren_list_exp → "(" list_exp ")"

array → ID "=" "{" exp "}"
      | ID "=" "{" "}"
      | ID "[" ID "]" "=" exp

assign → ID "=" exp  
  
call → ID paren_list_exp
     |ID "(" ")"

exp → exp "+" exp
      |exp "-" exp
      |exp "*" exp
      |exp "/" exp
      |exp "//" exp
      |exp "^" exp
      |exp "==" exp
      |exp "%" exp
      |exp AND exp
      |exp OR exp
      |exp NOT exp
      |exp ">" exp
      |exp "<" exp
      |exp "~=" exp
      |exp ">=" exp
      |exp "<=" exp
      |exp "&" exp
      |exp "|" exp
      |exp ".." exp
      |"#" exp
      |"-"exp
      |exp "~" exp
      |"~"exp
      |exp "," exp
      |exp "." exp
      |array
      |call
      |assign
      |LOCAL exp
      |STRING
      |NUMBER
      |ID
      |FALSE
      |NIL
      |TRUE
  
