from Abstract_Visitor import Abstract_Visitor
#https://github.com/andreluisms/FromASToWSML/blob/master/Visitor.py

# global Tab
tab = 0

def blank():
  p = ''
  for x in range(tab)
    p = p + ' '
  return p

class Visitor(AbstractVisitor):

  #programa
  def visitProgram(self, programDecl):
    if(programDecl.function):
      programDecl.function.accept(self)

    if(programDecl.local_function):
      programDecl.local_function.accept(self)

    if(programDecl.comand): 
      programDecl.comand.accept(self)
    
    print(blank(), programDecl.newline, end = '', sep = '')
    
    if(programDecl.program):
      programDecl.program.accept(self)
  
  #funtion e local function
  def visitFunction(self, functionDecl):
    print(blank(), 'function ', end = '', sep = '' )
    functionDecl.signature.accept(self)
    functionDecl.comands.accept(self)
    print(blank(),' end', end = '', sep = '')

  def visitLocalFunction(self, localFunctionDecl):
    print(blank(), 'local function ', end = '', sep = '')
    functionDecl.signature.accept(self)
    functionDecl.comands.accept(self)
    print(blank(),' end', end = '', sep = '')
  
  #signature
  def visitSignature(self, signatureDecl):
      print(blank(), signatureDecl.id, '( ' , end = '', sep = '')
      if(signatureDecl.sigparams != None):
        signatureDecl.sigparams.accept(self)
      print(blank(), ' )', end = '', sep = '')

  def visitSigparamSingle(self, singleSigParam):
    singleSigParam.id.accept(self)

  def visitCompoundSigparams(self, compoundSigParam):
    compoundSigParam.id.accept(self)
    print(' , ', end = '', sep = '')
    compoundSigParam.sigparams.accept(self)
    
  #comand/comands - body(corpo)
  def visitSingleComand(self, singleComand) :
      singleComand.comand.accept(self)
      singleComand.newline.accept(self)
  
  def visitorCompoundComand(self, compoundComand) :
      compoundComand.comand.accept(self)
      compoundComand.newline.accept(self)
      compoundComand.comands.accept(self)

#tipos de comand
  def visitComandIf1(self,comandIf1) :
    print(blank(), 'if ', end = '', sep = '')
    comandIf1.list_exp.accept(self)
    print(blank(),' then ', end = '', sep = '')
    comandIf1.comands.accept(self)
    printf(blank(), ' end', end = '', sep = '')
    
  def visitComandIf2(self, comandIf2) :
    print(blank(), 'if ', end = '' , sep = '')
    comandIf2.list_exp.accept(self)
    print(blank(), ' then ', end = '', sep = '')
    comandIf2.comands1.accept(self)
    print(blank(), ' else ', end = '', sep = '' )
    comandIf2.comands2.accept(self)
    print(blank(), ' end', end = '', sep = '')
    
  def visitComandIf3(self, comandIf3) :
    print(blank(), 'if ', end = '', sep = '')
    comandIf3.list_exp.accept(self)
    print(blank(), ' then ', end = '', sep = '')
    comandIf3.comands1.accept(self)
    comandIf3.elseif.accept(self)
    print(blank(), ' else ', end = '', sep = '')
    comandIf3.comands2.accept(self)
    print(blank(), ' end', end = '', sep = '')

  def visitSingleElseIf(self, singleElseIf) :
    print(blank(), 'elseif ', end = '', sep = '')
    singleElseIf.list_exp.accept(self)
    print(blank(), ' then ', end = '', sep = '')
    singleElseIf.comands.accept(self)

  def visitCompoundElseIf(self, compoundElseIf) :
    print(blank(), 'elseif ', end = '', sep = '')
    compoundElseIf.list_exp.accept(self)
    print(blank(), ' then ', end = '', sep = '')
    compoundElseIf.comands.accept(self)
    compoundElseIf.elseif.accept(self)
  
  def visitComandOtherComand(self, com_other_comand):
    com_other_comand.other_comand.accept(self)

#tipos de other_comand
  def visitOtherComandReturn(self, other_comandReturn) :
      print(blank(), 'return ', end='', sep='')
      other_comandReturn.exp.accept(self)
    
  def visitOtherComandExp(self, other_comandExp) :
    print(blank(),sep='',end='')
    other_comandExp.exp.accept(self)
    print('')  

  def visitOtherComandBreak(self, other_comandBreak):
    other_comandBreak.break.accept(self)
    
  def visitOtherComandWhile(self, other_comandWhile) :
    print(blank(), 'while ', end = '', sep = '')
    other_comandWhile.list_exp.accept(self)
    print(blank(), ' do ', end = '', sep = '')
    other_comandWhile.comands.accept(self)
    print(blank(), ' end', end = '', sep = '')

  def visitOtherComandForDo(self, other_comandForDo) :
    other_comandForDo.fordo.accept(self)

  def visitOtherComandForIn(self, other_comandForIn) :
    other_comandForIn.forin.accept(self)

  def visitForDo(self, forDo) :
    print(blank(), 'for ', end = '', sep = '')
    forDo.list_exp.accept(self)
    print(blank() ' do ', end = '', sep = '')
    forDo.comands.accept(self)
    print(blank(), 'end', end = '', sep = '')
    
  def visitForIn(self,forIn) :
    print(blank(), 'for ', end = '', sep = '')
    forIn.list_exp.accept(self)
    print(blank(), ' in ', end = '', sep = '')
    forIn.exp.accept(self)
    print(blank(), ' do ', exp = ''. sep = '')
    forIn.comands.accept(self)
    print(blank(), ' end', end = '', sep = '')


  def visitParensListExp(self, parenListExp):
    print('(', end = '', sep = '')
    parenListExp.exp.accept(self)
    print(')', end = '', sep = '')

  def visitListExp(self, listExp)
    listExp.exp.accept(self)

  def visitCall(self,call):
    print(blank(), call.id, ' (' ,end = '', sep = '')
    call.exp.accept(self)
    print(blank(), ' )', end = '', sep = '')

  def visitCallSimple(self, callS):
    callS.id.accept(self)
    print('()', end = '', sep = '')
  
  def visitArrayWithKeys(self, arrayWK):
    print('{ ', end = '', sep = '')
    arrayWK.exps.accept(self)
    print(' }', end = '', sep = '')

  def visitArrayKeys(self, arrayK):
    print('{}', end = '', sep = '')
    
  def visitArray_decl(self, array_decl):
    print(blank(), array_decl.id, ' (', end = '', sep = '')
    array_decl.exp.accept(self)
    print(' )', end = '', sep = '')

  def visitArray_declSimple(self, array_declS):
    print(blank(), array_declS.id, '()', end = '', sep = '')
    
    # definições de expressões
  def visitOrExp(self, orExp):
    orExp.exp1.accept(self)
    print(' or ', end='')
    orExp.exp2.accept(self)
  
  def visitAndExp(self, andExp):
    andExp.exp1.accept(self)
    print(' and ', end='')
    andExp.exp2.accept(self)
  
  def visitLessThanExp(self, lessThanExp):
    lessThanExp.exp1.accept(self)
    print(' < ', end='')
    lessThanExp.exp2.accept(self)
  
  def visitBiggerThanExp(self, biggerThanExp):
    biggerThanExp.exp1.accept(self)
    print(' > ', end='')
    biggerThanExp.exp2.accept(self)
  
  def visitLessEqualExp(self, lessEqualExp):
    lessEqualExp.exp1.accept(self)
    print(' <= ', end='')
    lessEqualExp.exp2.accept(self)
  
  def visitBiggerEqualExp(self, biggerEqualExp):
    biggerEqualExp.exp1.accept(self)
    print(' >= ', end='')
    biggerEqualExp.exp2.accept(self)
  
  def visitDifExp(self, difExp):
    difExp.exp1.accept(self)
    print(' ~= ', end='')
    difExp.exp2.accept(self)
  
  def visitEqualExp(self, equalExp):
    equalExp.exp1.accept(self)
    print(' == ', end='')
    equalExp.exp2.accept(self)
  
  def visitBitwiseExecOrExp(self, bitwiseExecOrExp):
    bitwiseExecOrExp.exp1.accept(self)
    print(' ~ ', end='')
    bitwiseExecOrExp.exp2.accept(self)
  
  def visitBitwiseAndExp(self, bitwiseAndExp):
    bitwiseAndExp.exp1.accept(self)
    print(' & ', end='')
    bitwiseAndExp.exp2.accept(self)
  
  def visitConcatenationExp(self, concatenationExp):
    concatenationExp.exp1.accept(self)
    print(' .. ', end='')
    concatenationExp.exp2.accept(self)
  
  def visitSumExp(self, sumExp):
    sumExp.exp1.accept(self)
    print(' + ', end='')
    sumExp.exp2.accept(self)
  
  def visitModuleExp(self, moduleExp):
    moduleExp.exp1.accept(self)
    print(' % ', end='')
    moduleExp.exp2.accept(self)
  
  def visitDivExp(self, divExp):
    divExp.exp1.accept(self)
    print(' / ', end='')
    divExp.exp2.accept(self)
  
  def visitDivIntExp(self, divIntExp):
    divIntExp.exp1.accept(self)
    print(' // ', end='')
    divIntExp.exp2.accept(self)
  
  def visitMultExp(self, mulExp):
    mulExp.exp1.accept(self)
    print(' * ', end='')
    mulExp.exp2.accept(self)
  
  def visitNotExp(self, notExp):
    notExp.exp1.accept(self)
    print(' not ', end='')
    notExp.exp2.accept(self)
  
  def visitDenialExp(self, denialExp):
    print(' - ', end='')
    denialExp.exp1.accept(self)
  
  def visitUnaryBitwiseNotExp(self, unaryBitwiseNotExp):
    print(' ~ ', end='')
    unaryBitwiseNotExp.exp1.accept(self)
  
  def visitPowExp(self, powExp):
    powExp.exp1.accept(self)
    print(' ^ ', end='')
    powExp.exp2.accept(self)
  
  def visitDotExp(self, dotExp):
    powExp.exp1.accept(self)
    print('.', end='')
    powExp.exp2.accept(self)
  
  def visitNumberExp(self, numberExp):
    print(numberExp.numberValue, end='')
  
  def visitStringExp(self, stringExp):
    print(stringExp.stringValue, end='')
   
  def visitIdExp(self, idExp):
    print(idExp.id, end='')
    
  def visitLocalIdExp(self, localIdExp):
    print(localIdExp.localId, end='')
   
  def visitTrueExp(self, trueExp):
    print(trueExp.trueValue, end='')
  
  def visitFalseExp(self, falseExp):
    print(falseExp.falseValue, end='')

def visitBitwiseOrExp(self, bitwiseOrExp):
  bitwiseOrExp.exp1.accept(self)
    print(' | ', end='')
    bitwiseOrExp.exp2.accept(self)

def visitSubExp(self, subExp):
    subExp.exp1.accept(self)
    print(' - ', end='')
    subExp.exp2.accept(self)

  def visitLenghtExp(self, lenghtExp):
      print(' # ', end='')
      lenghtExp.exp1.accept(self)

    
    
    

