
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BIGGER_EQUAL BIGGER_THAN BITWISE_AND BITWISE_EXC_OR BITWISE_OR BREAK COLON COMMA COMMENT CONCATENATION DENIAL DIF DIV DIV_INT DO DOT ELSE ELSEIF END EQUAL FALSE FOR FUNCTION ID IF IN LCOCHETE LENGHT LESS_EQUAL LESS_THAN LKEY LOCAL LPAREN MODULE MULT NEWLINE NIL NOT NUMBER OR POW RCOCHETE RETURN RKEY RPAREN SEMICOLON STRING SUB SUM THEN TRUE UNARY_BITWISE_NOT WHILEprogram : comand NEWLINEprogram : function NEWLINEprogram : local_function NEWLINEprogram : comand NEWLINE programprogram : function NEWLINE program program : local_function NEWLINE programfunction : FUNCTION signature comands ENDlocal_function : LOCAL FUNCTION signature comands ENDsignature : ID LPAREN sigparams RPARENsignature : ID LPAREN RPARENsigparams : ID\n               | ID COMMA sigparamscomands : comand NEWLINEcomands : comand NEWLINE comands comand : IF list_exp THEN comands ENDcomand : IF list_exp THEN comands ELSE comands END comand : IF list_exp THEN comands elseif ELSE comandscomand : other_comandelseif : ELSEIF list_exp THEN comandselseif : ELSEIF list_exp THEN comands elseifother_comand : WHILE list_exp DO comands ENDother_comand : fordoother_comand : expother_comand : forinother_comand : RETURN expother_comand : BREAKfordo : FOR list_exp DO comands ENDforin : FOR list_exp IN exp DO comands ENDlist_exp : LPAREN exp RPAREN \n              | expcall : ID LPAREN exp RPAREN\n          | ID LPAREN RPARENarray : LKEY exp RKEY\n           | LKEY RKEY\n           | ID LCOCHETE exp RCOCHETE\n           | ID LCOCHETE RCOCHETEexp : exp ASSIGN exp_1\n           | exp_1exp_1 : exp_1 OR exp_2\n           | exp_2exp_2 : exp_2 AND exp_3\n           | exp_3exp_3 : exp_3 LESS_THAN exp_4\n           | exp_4exp_4 : exp_4 BIGGER_THAN exp_5\n           | exp_5exp_5 : exp_5 LESS_EQUAL exp_6\n           | exp_6exp_6 : exp_6 BIGGER_EQUAL exp_7\n           | exp_7exp_7 : exp_7 DIF exp_8\n           | exp_8exp_8 : exp_8 EQUAL exp_9\n           | exp_9exp_9 : exp_9 BITWISE_OR exp_10\n           | exp_10exp_10 : exp_10 BITWISE_EXC_OR exp_11\n            | exp_11exp_11 : exp_11 BITWISE_AND exp_12\n            | exp_12exp_12 : exp_12 CONCATENATION exp_13\n           | exp_13exp_13 : exp_13 SUB exp_14\n           | exp_14exp_14 : exp_14 SUM exp_15\n           | exp_15exp_15 : exp_15 MODULE exp_16\n           | exp_16exp_16 : exp_16 DIV_INT exp_17\n            | exp_17exp_17 : exp_17 DIV exp_18\n            | exp_18exp_18 : exp_18 MULT exp_19\n            | exp_19exp_19 : exp_19 NOT exp_20\n            | exp_20exp_20 : DENIAL exp_20\n            | exp_21exp_21 : UNARY_BITWISE_NOT exp_21\n            | exp_22exp_22 : LENGHT exp_22\n            | exp_23exp_23 : exp_23 POW exp_24\n            | exp_24exp_24 : exp_24 COMMA exp_25\n            | exp_24 DOT exp_25\n            | array\n            | call\n            | exp_25exp_25 : NUMBER \n            | STRING \n            | LOCAL ID\n            | ID\n            | NIL\n            | TRUE\n            | FALSE'
    
_lr_action_items = {'IF':([0,53,54,55,60,100,105,106,108,141,144,152,157,161,163,169,],[5,5,5,5,5,5,5,5,5,5,-10,5,-9,5,5,5,]),'FUNCTION':([0,8,53,54,55,],[7,62,7,7,7,]),'LOCAL':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,95,96,100,105,106,108,109,141,144,152,154,157,161,163,169,],[8,59,59,59,59,59,59,59,59,8,8,8,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-10,59,59,-9,59,59,59,]),'WHILE':([0,53,54,55,60,100,105,106,108,141,144,152,157,161,163,169,],[9,9,9,9,9,9,9,9,9,9,-10,9,-9,9,9,9,]),'RETURN':([0,53,54,55,60,100,105,106,108,141,144,152,157,161,163,169,],[13,13,13,13,13,13,13,13,13,13,-10,13,-9,13,13,13,]),'BREAK':([0,53,54,55,60,100,105,106,108,141,144,152,157,161,163,169,],[14,14,14,14,14,14,14,14,14,14,-10,14,-9,14,14,14,]),'FOR':([0,53,54,55,60,100,105,106,108,141,144,152,157,161,163,169,],[15,15,15,15,15,15,15,15,15,15,-10,15,-9,15,15,15,]),'DENIAL':([0,5,9,13,15,36,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,96,100,105,106,108,109,141,144,152,154,157,161,163,169,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-10,36,36,-9,36,36,36,]),'UNARY_BITWISE_NOT':([0,5,9,13,15,36,38,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,96,100,105,106,108,109,141,144,152,154,157,161,163,169,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-10,38,38,-9,38,38,38,]),'LENGHT':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,96,100,105,106,108,109,141,144,152,154,157,161,163,169,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-10,40,40,-9,40,40,40,]),'LKEY':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,95,96,100,105,106,108,109,141,144,152,154,157,161,163,169,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-10,46,46,-9,46,46,46,]),'ID':([0,5,7,8,9,13,15,36,38,40,46,53,54,55,57,59,60,62,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,95,96,100,104,105,106,108,109,141,144,152,154,156,157,161,163,169,],[47,47,61,63,47,47,47,47,47,47,47,47,47,47,47,63,47,61,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,131,131,47,47,47,142,47,47,47,47,47,-10,47,47,142,-9,47,47,47,]),'NUMBER':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,95,96,100,105,106,108,109,141,144,152,154,157,161,163,169,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-10,48,48,-9,48,48,48,]),'STRING':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,95,96,100,105,106,108,109,141,144,152,154,157,161,163,169,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-10,49,49,-9,49,49,49,]),'NIL':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,95,96,100,105,106,108,109,141,144,152,154,157,161,163,169,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-10,50,50,-9,50,50,50,]),'TRUE':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,95,96,100,105,106,108,109,141,144,152,154,157,161,163,169,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-10,51,51,-9,51,51,51,]),'FALSE':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,95,96,100,105,106,108,109,141,144,152,154,157,161,163,169,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-10,52,52,-9,52,52,52,]),'$end':([1,53,54,55,97,98,99,],[0,-1,-2,-3,-4,-5,-6,]),'NEWLINE':([2,3,4,6,10,11,12,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,66,87,88,89,94,103,107,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,140,141,149,150,151,155,158,159,160,167,168,170,],[53,54,55,-18,-22,-23,-24,-26,-38,-40,-42,-44,-46,-48,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-25,-77,-79,-81,-34,141,-37,-39,-41,-43,-45,-47,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-7,-13,-35,-31,-15,-14,-8,-21,-27,-16,-17,-28,]),'LPAREN':([5,9,15,47,61,154,],[57,57,57,96,104,57,]),'ASSIGN':([11,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,58,63,66,87,88,89,93,94,101,107,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,148,149,150,],[65,-38,-40,-42,-44,-46,-48,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,65,-92,65,-77,-79,-81,65,-34,65,-37,-39,-41,-43,-45,-47,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,65,-36,65,-32,65,-35,-31,]),'THEN':([16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,56,58,63,87,88,89,94,107,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,139,149,150,164,],[-38,-40,-42,-44,-46,-48,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,100,-30,-92,-77,-79,-81,-34,-37,-39,-41,-43,-45,-47,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-29,-35,-31,169,]),'DO':([16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,58,63,64,67,87,88,89,94,107,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,139,148,149,150,],[-38,-40,-42,-44,-46,-48,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-30,-92,106,108,-77,-79,-81,-34,-37,-39,-41,-43,-45,-47,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-29,161,-35,-31,]),'IN':([16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,58,63,67,87,88,89,94,107,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,139,149,150,],[-38,-40,-42,-44,-46,-48,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-30,-92,109,-77,-79,-81,-34,-37,-39,-41,-43,-45,-47,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-29,-35,-31,]),'RKEY':([16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,46,47,48,49,50,51,52,63,87,88,89,93,94,107,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[-38,-40,-42,-44,-46,-48,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,94,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,133,-34,-37,-39,-41,-43,-45,-47,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'RPAREN':([16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,96,101,104,107,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,136,137,142,143,149,150,165,],[-38,-40,-42,-44,-46,-48,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,137,139,144,-37,-39,-41,-43,-45,-47,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,150,-32,-11,157,-35,-31,-12,]),'RCOCHETE':([16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,95,107,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,149,150,],[-38,-40,-42,-44,-46,-48,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,135,-37,-39,-41,-43,-45,-47,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,149,-36,-32,-35,-31,]),'OR':([16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,107,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[68,-40,-42,-44,-46,-48,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,68,-39,-41,-43,-45,-47,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'AND':([17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[69,-42,-44,-46,-48,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,69,-41,-43,-45,-47,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'LESS_THAN':([18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[70,-44,-46,-48,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,70,-43,-45,-47,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'BIGGER_THAN':([19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[71,-46,-48,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,71,-45,-47,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'LESS_EQUAL':([20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[72,-48,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,72,-47,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'BIGGER_EQUAL':([21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[73,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,73,-49,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'DIF':([22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[74,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,74,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'EQUAL':([23,24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[75,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,75,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'BITWISE_OR':([24,25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[76,-56,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,76,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'BITWISE_EXC_OR':([25,26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[77,-58,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,77,-57,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'BITWISE_AND':([26,27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[78,-60,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,78,-59,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'CONCATENATION':([27,28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[79,-62,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,79,-61,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'SUB':([28,29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[80,-64,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,80,-63,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'SUM':([29,30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,122,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[81,-66,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,81,-65,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'MODULE':([30,31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,123,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[82,-68,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,82,-67,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'DIV_INT':([31,32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,124,125,126,127,128,129,130,131,132,133,135,137,149,150,],[83,-70,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,83,-69,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'DIV':([32,33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,125,126,127,128,129,130,131,132,133,135,137,149,150,],[84,-72,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,84,-71,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'MULT':([33,34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,126,127,128,129,130,131,132,133,135,137,149,150,],[85,-74,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,85,-73,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'NOT':([34,35,37,39,41,42,43,44,45,47,48,49,50,51,52,63,87,88,89,94,127,128,129,130,131,132,133,135,137,149,150,],[86,-76,-78,-80,-82,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-77,-79,-81,-34,86,-75,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'POW':([41,42,43,44,45,47,48,49,50,51,52,63,94,129,130,131,132,133,135,137,149,150,],[90,-84,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-34,-83,-85,-93,-86,-33,-36,-32,-35,-31,]),'COMMA':([42,43,44,45,47,48,49,50,51,52,63,94,129,130,131,132,133,135,137,142,149,150,],[91,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-34,91,-85,-93,-86,-33,-36,-32,156,-35,-31,]),'DOT':([42,43,44,45,47,48,49,50,51,52,63,94,129,130,131,132,133,135,137,149,150,],[92,-89,-87,-88,-93,-90,-91,-94,-95,-96,-92,-34,92,-85,-93,-86,-33,-36,-32,-35,-31,]),'LCOCHETE':([47,],[95,]),'END':([102,138,141,145,146,147,155,162,166,],[140,151,-13,158,159,160,-14,167,170,]),'ELSE':([138,141,153,155,171,172,],[152,-13,163,-14,-19,-20,]),'ELSEIF':([138,141,155,171,],[154,-13,-14,154,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,53,54,55,],[1,97,98,99,]),'comand':([0,53,54,55,60,100,105,106,108,141,152,161,163,169,],[2,2,2,2,103,103,103,103,103,103,103,103,103,103,]),'function':([0,53,54,55,],[3,3,3,3,]),'local_function':([0,53,54,55,],[4,4,4,4,]),'other_comand':([0,53,54,55,60,100,105,106,108,141,152,161,163,169,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'fordo':([0,53,54,55,60,100,105,106,108,141,152,161,163,169,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'exp':([0,5,9,13,15,46,53,54,55,57,60,95,96,100,105,106,108,109,141,152,154,161,163,169,],[11,58,58,66,58,93,11,11,11,101,11,134,136,11,11,11,11,148,11,11,58,11,11,11,]),'forin':([0,53,54,55,60,100,105,106,108,141,152,161,163,169,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'exp_1':([0,5,9,13,15,46,53,54,55,57,60,65,95,96,100,105,106,108,109,141,152,154,161,163,169,],[16,16,16,16,16,16,16,16,16,16,16,107,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'exp_2':([0,5,9,13,15,46,53,54,55,57,60,65,68,95,96,100,105,106,108,109,141,152,154,161,163,169,],[17,17,17,17,17,17,17,17,17,17,17,17,110,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'exp_3':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,95,96,100,105,106,108,109,141,152,154,161,163,169,],[18,18,18,18,18,18,18,18,18,18,18,18,18,111,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'exp_4':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,95,96,100,105,106,108,109,141,152,154,161,163,169,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,112,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'exp_5':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,95,96,100,105,106,108,109,141,152,154,161,163,169,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,113,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'exp_6':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,95,96,100,105,106,108,109,141,152,154,161,163,169,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,114,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'exp_7':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,73,95,96,100,105,106,108,109,141,152,154,161,163,169,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,115,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'exp_8':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,73,74,95,96,100,105,106,108,109,141,152,154,161,163,169,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,116,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'exp_9':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,95,96,100,105,106,108,109,141,152,154,161,163,169,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,117,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'exp_10':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,95,96,100,105,106,108,109,141,152,154,161,163,169,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,118,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'exp_11':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,95,96,100,105,106,108,109,141,152,154,161,163,169,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,119,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'exp_12':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,95,96,100,105,106,108,109,141,152,154,161,163,169,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,120,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'exp_13':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,95,96,100,105,106,108,109,141,152,154,161,163,169,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,121,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'exp_14':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,95,96,100,105,106,108,109,141,152,154,161,163,169,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,122,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'exp_15':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,95,96,100,105,106,108,109,141,152,154,161,163,169,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,123,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'exp_16':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,95,96,100,105,106,108,109,141,152,154,161,163,169,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,124,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'exp_17':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,95,96,100,105,106,108,109,141,152,154,161,163,169,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,125,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'exp_18':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,95,96,100,105,106,108,109,141,152,154,161,163,169,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,126,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'exp_19':([0,5,9,13,15,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,95,96,100,105,106,108,109,141,152,154,161,163,169,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,127,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'exp_20':([0,5,9,13,15,36,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,96,100,105,106,108,109,141,152,154,161,163,169,],[35,35,35,35,35,87,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,128,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'exp_21':([0,5,9,13,15,36,38,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,96,100,105,106,108,109,141,152,154,161,163,169,],[37,37,37,37,37,37,88,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'exp_22':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,96,100,105,106,108,109,141,152,154,161,163,169,],[39,39,39,39,39,39,39,89,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'exp_23':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,95,96,100,105,106,108,109,141,152,154,161,163,169,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'exp_24':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,95,96,100,105,106,108,109,141,152,154,161,163,169,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,129,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'exp_25':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,95,96,100,105,106,108,109,141,152,154,161,163,169,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,130,132,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'array':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,95,96,100,105,106,108,109,141,152,154,161,163,169,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'call':([0,5,9,13,15,36,38,40,46,53,54,55,57,60,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,95,96,100,105,106,108,109,141,152,154,161,163,169,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'list_exp':([5,9,15,154,],[56,64,67,164,]),'signature':([7,62,],[60,105,]),'comands':([60,100,105,106,108,141,152,161,163,169,],[102,138,145,146,147,155,162,166,168,171,]),'sigparams':([104,156,],[143,165,]),'elseif':([138,171,],[153,172,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> comand NEWLINE','program',2,'p_program1','Analise_Sintatico.py',10),
  ('program -> function NEWLINE','program',2,'p_program2','Analise_Sintatico.py',14),
  ('program -> local_function NEWLINE','program',2,'p_program3','Analise_Sintatico.py',18),
  ('program -> comand NEWLINE program','program',3,'p_program4','Analise_Sintatico.py',23),
  ('program -> function NEWLINE program','program',3,'p_program5','Analise_Sintatico.py',27),
  ('program -> local_function NEWLINE program','program',3,'p_program6','Analise_Sintatico.py',31),
  ('function -> FUNCTION signature comands END','function',4,'p_function','Analise_Sintatico.py',36),
  ('local_function -> LOCAL FUNCTION signature comands END','local_function',5,'p_local_function','Analise_Sintatico.py',40),
  ('signature -> ID LPAREN sigparams RPAREN','signature',4,'p_signature1','Analise_Sintatico.py',45),
  ('signature -> ID LPAREN RPAREN','signature',3,'p_signature2','Analise_Sintatico.py',49),
  ('sigparams -> ID','sigparams',1,'p_sigparams','Analise_Sintatico.py',54),
  ('sigparams -> ID COMMA sigparams','sigparams',3,'p_sigparams','Analise_Sintatico.py',55),
  ('comands -> comand NEWLINE','comands',2,'p_comands1','Analise_Sintatico.py',61),
  ('comands -> comand NEWLINE comands','comands',3,'p_comands2','Analise_Sintatico.py',66),
  ('comand -> IF list_exp THEN comands END','comand',5,'p_comand1','Analise_Sintatico.py',71),
  ('comand -> IF list_exp THEN comands ELSE comands END','comand',7,'p_comand2','Analise_Sintatico.py',75),
  ('comand -> IF list_exp THEN comands elseif ELSE comands','comand',7,'p_comand3','Analise_Sintatico.py',79),
  ('comand -> other_comand','comand',1,'p_comand4','Analise_Sintatico.py',83),
  ('elseif -> ELSEIF list_exp THEN comands','elseif',4,'p_elseif1','Analise_Sintatico.py',88),
  ('elseif -> ELSEIF list_exp THEN comands elseif','elseif',5,'p_elseif2','Analise_Sintatico.py',92),
  ('other_comand -> WHILE list_exp DO comands END','other_comand',5,'p_other_comand1','Analise_Sintatico.py',97),
  ('other_comand -> fordo','other_comand',1,'p_other_comand2','Analise_Sintatico.py',101),
  ('other_comand -> exp','other_comand',1,'p_other_comand3','Analise_Sintatico.py',105),
  ('other_comand -> forin','other_comand',1,'p_other_comand4','Analise_Sintatico.py',109),
  ('other_comand -> RETURN exp','other_comand',2,'p_other_comand5','Analise_Sintatico.py',113),
  ('other_comand -> BREAK','other_comand',1,'p_other_comand6','Analise_Sintatico.py',117),
  ('fordo -> FOR list_exp DO comands END','fordo',5,'p_fordo','Analise_Sintatico.py',121),
  ('forin -> FOR list_exp IN exp DO comands END','forin',7,'p_forin','Analise_Sintatico.py',125),
  ('list_exp -> LPAREN exp RPAREN','list_exp',3,'p_list_exp','Analise_Sintatico.py',130),
  ('list_exp -> exp','list_exp',1,'p_list_exp','Analise_Sintatico.py',131),
  ('call -> ID LPAREN exp RPAREN','call',4,'p_call','Analise_Sintatico.py',136),
  ('call -> ID LPAREN RPAREN','call',3,'p_call','Analise_Sintatico.py',137),
  ('array -> LKEY exp RKEY','array',3,'p_array','Analise_Sintatico.py',142),
  ('array -> LKEY RKEY','array',2,'p_array','Analise_Sintatico.py',143),
  ('array -> ID LCOCHETE exp RCOCHETE','array',4,'p_array','Analise_Sintatico.py',144),
  ('array -> ID LCOCHETE RCOCHETE','array',3,'p_array','Analise_Sintatico.py',145),
  ('exp -> exp ASSIGN exp_1','exp',3,'p_exp','Analise_Sintatico.py',150),
  ('exp -> exp_1','exp',1,'p_exp','Analise_Sintatico.py',151),
  ('exp_1 -> exp_1 OR exp_2','exp_1',3,'p_exp_1','Analise_Sintatico.py',155),
  ('exp_1 -> exp_2','exp_1',1,'p_exp_1','Analise_Sintatico.py',156),
  ('exp_2 -> exp_2 AND exp_3','exp_2',3,'p_exp_2','Analise_Sintatico.py',160),
  ('exp_2 -> exp_3','exp_2',1,'p_exp_2','Analise_Sintatico.py',161),
  ('exp_3 -> exp_3 LESS_THAN exp_4','exp_3',3,'p_exp_3','Analise_Sintatico.py',165),
  ('exp_3 -> exp_4','exp_3',1,'p_exp_3','Analise_Sintatico.py',166),
  ('exp_4 -> exp_4 BIGGER_THAN exp_5','exp_4',3,'p_exp_4','Analise_Sintatico.py',170),
  ('exp_4 -> exp_5','exp_4',1,'p_exp_4','Analise_Sintatico.py',171),
  ('exp_5 -> exp_5 LESS_EQUAL exp_6','exp_5',3,'p_exp_5','Analise_Sintatico.py',175),
  ('exp_5 -> exp_6','exp_5',1,'p_exp_5','Analise_Sintatico.py',176),
  ('exp_6 -> exp_6 BIGGER_EQUAL exp_7','exp_6',3,'p_exp_6','Analise_Sintatico.py',180),
  ('exp_6 -> exp_7','exp_6',1,'p_exp_6','Analise_Sintatico.py',181),
  ('exp_7 -> exp_7 DIF exp_8','exp_7',3,'p_exp_7','Analise_Sintatico.py',185),
  ('exp_7 -> exp_8','exp_7',1,'p_exp_7','Analise_Sintatico.py',186),
  ('exp_8 -> exp_8 EQUAL exp_9','exp_8',3,'p_exp_8','Analise_Sintatico.py',190),
  ('exp_8 -> exp_9','exp_8',1,'p_exp_8','Analise_Sintatico.py',191),
  ('exp_9 -> exp_9 BITWISE_OR exp_10','exp_9',3,'p_exp_9','Analise_Sintatico.py',195),
  ('exp_9 -> exp_10','exp_9',1,'p_exp_9','Analise_Sintatico.py',196),
  ('exp_10 -> exp_10 BITWISE_EXC_OR exp_11','exp_10',3,'p_exp_10','Analise_Sintatico.py',200),
  ('exp_10 -> exp_11','exp_10',1,'p_exp_10','Analise_Sintatico.py',201),
  ('exp_11 -> exp_11 BITWISE_AND exp_12','exp_11',3,'p_exp_11','Analise_Sintatico.py',205),
  ('exp_11 -> exp_12','exp_11',1,'p_exp_11','Analise_Sintatico.py',206),
  ('exp_12 -> exp_12 CONCATENATION exp_13','exp_12',3,'p_exp_12','Analise_Sintatico.py',210),
  ('exp_12 -> exp_13','exp_12',1,'p_exp_12','Analise_Sintatico.py',211),
  ('exp_13 -> exp_13 SUB exp_14','exp_13',3,'p_exp_13','Analise_Sintatico.py',215),
  ('exp_13 -> exp_14','exp_13',1,'p_exp_13','Analise_Sintatico.py',216),
  ('exp_14 -> exp_14 SUM exp_15','exp_14',3,'p_exp_14','Analise_Sintatico.py',220),
  ('exp_14 -> exp_15','exp_14',1,'p_exp_14','Analise_Sintatico.py',221),
  ('exp_15 -> exp_15 MODULE exp_16','exp_15',3,'p_exp_15','Analise_Sintatico.py',225),
  ('exp_15 -> exp_16','exp_15',1,'p_exp_15','Analise_Sintatico.py',226),
  ('exp_16 -> exp_16 DIV_INT exp_17','exp_16',3,'p_exp_16','Analise_Sintatico.py',230),
  ('exp_16 -> exp_17','exp_16',1,'p_exp_16','Analise_Sintatico.py',231),
  ('exp_17 -> exp_17 DIV exp_18','exp_17',3,'p_exp_17','Analise_Sintatico.py',235),
  ('exp_17 -> exp_18','exp_17',1,'p_exp_17','Analise_Sintatico.py',236),
  ('exp_18 -> exp_18 MULT exp_19','exp_18',3,'p_exp_18','Analise_Sintatico.py',240),
  ('exp_18 -> exp_19','exp_18',1,'p_exp_18','Analise_Sintatico.py',241),
  ('exp_19 -> exp_19 NOT exp_20','exp_19',3,'p_exp_19','Analise_Sintatico.py',245),
  ('exp_19 -> exp_20','exp_19',1,'p_exp_19','Analise_Sintatico.py',246),
  ('exp_20 -> DENIAL exp_20','exp_20',2,'p_exp_20','Analise_Sintatico.py',250),
  ('exp_20 -> exp_21','exp_20',1,'p_exp_20','Analise_Sintatico.py',251),
  ('exp_21 -> UNARY_BITWISE_NOT exp_21','exp_21',2,'p_exp_21','Analise_Sintatico.py',255),
  ('exp_21 -> exp_22','exp_21',1,'p_exp_21','Analise_Sintatico.py',256),
  ('exp_22 -> LENGHT exp_22','exp_22',2,'p_exp_22','Analise_Sintatico.py',260),
  ('exp_22 -> exp_23','exp_22',1,'p_exp_22','Analise_Sintatico.py',261),
  ('exp_23 -> exp_23 POW exp_24','exp_23',3,'p_exp_23','Analise_Sintatico.py',265),
  ('exp_23 -> exp_24','exp_23',1,'p_exp_23','Analise_Sintatico.py',266),
  ('exp_24 -> exp_24 COMMA exp_25','exp_24',3,'p_exp_24','Analise_Sintatico.py',270),
  ('exp_24 -> exp_24 DOT exp_25','exp_24',3,'p_exp_24','Analise_Sintatico.py',271),
  ('exp_24 -> array','exp_24',1,'p_exp_24','Analise_Sintatico.py',272),
  ('exp_24 -> call','exp_24',1,'p_exp_24','Analise_Sintatico.py',273),
  ('exp_24 -> exp_25','exp_24',1,'p_exp_24','Analise_Sintatico.py',274),
  ('exp_25 -> NUMBER','exp_25',1,'p_exp_25','Analise_Sintatico.py',278),
  ('exp_25 -> STRING','exp_25',1,'p_exp_25','Analise_Sintatico.py',279),
  ('exp_25 -> LOCAL ID','exp_25',2,'p_exp_25','Analise_Sintatico.py',280),
  ('exp_25 -> ID','exp_25',1,'p_exp_25','Analise_Sintatico.py',281),
  ('exp_25 -> NIL','exp_25',1,'p_exp_25','Analise_Sintatico.py',282),
  ('exp_25 -> TRUE','exp_25',1,'p_exp_25','Analise_Sintatico.py',283),
  ('exp_25 -> FALSE','exp_25',1,'p_exp_25','Analise_Sintatico.py',284),
]