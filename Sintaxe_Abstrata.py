from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

#https://github.com/andreluisms/FromASToWSML/blob/master/SintaxeAbstrata.py



# Definição de Programa
class ProgramAbstrata(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class Program(ProgramAbstrata):
  def _init_(self,comand, function, local_function, program):
    self.comand = comand
    self.function = function
    self.local_function = local_function
    self.program = program
  def accept(self, visitor):
    return visitor.visitProgram(self)
    
# Definição de Função
class FunctionAbstrata(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class Function(FunctionAbstrata):
  def _init_(self, signature, comands):
    self.signature = signature
    self.comands = comands
  def accept(self, visitor):
    return visitor.visitFunction(self)
    
class LocalFunctionAbstrata(metaclass = ABCMETA):
  @abstractmethod
  def accept(self, visitor):
    pass

class LocalFunction(LocalFunctionAbstrata):
  def _init_ (self, signature, comands):
    self.signature = signature
    self.comands = comands
    def accept(self,visitor):
      return visitor.visitLocalFunction(self)
  
# Assinatura 
class SignatureAbstrata(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class Signature(SignatureAbstrata):
  def _init_(self, id, sigParams):
    self.id = id
    self.sigParams = sigParams
  def accept(self, visitor):
    return visitor.visitSignature(self)

class SingleSigparamsAbstrata(metaclass=ABCMeta):
  @abstractmethod
  def accept (self, visitor):
    pass
class SingleSigparams(ComandAbstrata):
  def _init_(self,id):
    self.id = id
  def accept(self, visitor):
    return visitor.visitSigparamSingle(self)

class CompoundSigparamsAbstrata(metaclass=ABCMeta):
  @abstractmethod
  def accept (self, visitor):
    pass
class CompoundSigparams(ComandAbstrata):
  def _init_(self,id, sigparams):
     self.id = id
     self.sigparams = sigparams
  def accept(self, visitor):
     return visitor.visitorCompoundSigparams(self)
    
class ComandAbstrata(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class SingleComand(ComandAbstrata):
  def _init_(self,comand,newline):
    self.comand = comand
    self.newline = newline
  def accept(self, visitor):
    return visitor.visitSingleComand(self)

class ComandCompound(ComandAbstrata):
  def _init_(self,comand, newline, comands):
     self.comand = comand
     self.newline = newline
     self.comands = comands
  def accept(self, visitor):
     return visitor.visitorCompoundComand(self)
    
class ComandIfAbstract(metaclass=ABCMeta):
   @abstractmethod
   def accept(self, visitor):
     pass

class ComandIf1(ComandIfAbstract):
  def _init_(self,listExp, comands):
    self.list_exp = listExp
    self.comands = comands
  def accept(self,visitor): 
    return visitor.visitorComandIf1(self)

class ComandIf2(ComandIfAbstract):
  def _init_(self, listExp, comands1, comands2):
    self.listExp = listExp
    self.comands1 = comands1
    self.comands2 = comands2
  def accept(self, visitor):
    return visitor.visitorComandIf2

class ComandIf3(ComandIfAbstract):
  def _init_(self, listExp, comands1, elseIf, comands2):
    self.listExp = listExp
    self.comands1 = comands1
    self.elseIf = elseIf
    self.comands2 =  comands2
  def accept (self, visitor):
    return visitor.visitorComandIf3

class ComandElseIfAbstract(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

 class SingleElseIf(ComandElseIfAbstract):
  def _init_(self, listExp, comands):
    self.listExp = listExp
    self.comands = comands
  def accept(self,visitor):
    return visitor.visitSingleElseIf(self)

 class CompoundElseIf(ComandElseIfAbstract):
  def _init_(self, listExp, comands, elseIf):
    self.listExp = listExp
    self.comands = comands
    self.elseIf = elseIf
  def accept(self, visitor):
    return visitor.visitCompoundElseIf(self)

 class ComandOtherComandAbstract(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ComandOtherComand (ComandOtherComandAbstract):
  def _init_ (self, other_comand):
    self.othercomand
  def accept(self, visitor):
    return visitor.visitComandOtherComand(self)

class ComandOtherComandReturn(ComandOtherComandAbstract):
  def _init_(self, exp):
    self.exp = exp 
  def accept(self, visitor):
    return visitor.visitOtherComandReturn(self)

class ComandOtherComandExp(ComandOtherComandAbstract):
  def _init_(self, exp):
    self.exp = exp 
  def accept(self, visitor):
    return visitor.visitOtherComandExp(self)

class ComandOtherComandBreak(ComandOtherComandAbstract):
  def _init_ (self, break):
    self.break = break
    def accept(self, visitor):
      return visitor.visitOtherComandBreak(self)

class ComandOtherComandWhile(ComandOtherComandAbstract):
  def _init_(self, listExp, comands):
    self.listExp = listExp 
    self.comands = comands
  def accept(self, visitor):
    return visitor.visitOtherComandWhile(self)

class OtherComandForDo(ComandOtherComandAbstract):
  def _init_(self, forDo):
    self.forDo = forDo
  def accept(self, visitor):
    return visitor.visitorOtherComandForDo

class OtherComandForIn(ComandOtherComandAbstract):
  def _init_(self,forIn):
    self.forIn = forIn
  def accept(self, visitor):
    return visitor.visitOtherComandForIn(self)
    
class ComandForDoAbstract(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ComandFordo(ComandForDoAbstract):
  def _init_(self, lisExp, comands):
    self.listExp = listExp
    self.comands = comands
  def accept(self, visitor):
    return visitor.visitForDo(self)

class ComandForInAbstract(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ComandForIn(ComandForInAbstract):
  def _init_(self, lisExp, exp, comands):
    self.listExp = listExp
    self.exp = exp
    self.comands = comands
  def accept(self, visitor):
    return visitor.visitForIn(self)

class ParensListExpAbstrata(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ParensListExp(ParensListExpAbstrata):
  def _init_(self, exp):
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitParensListExp(self)

class ListExpAbstrata(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ListExp(VisitListExpAbstrata):
  def _init_(self, exp):
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitListExp(self)

class CallAbstrata(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class Call(VisitCallAbstrata):
  def _init_(self, exp):
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitCall(self)

class CallSimple(VisitCallAbstrata):
  def _init_(self, id):
    self.id = id
  def accept(self, visitor):
    return visitor.visitCallSimple(self)

class ArrayAbstrata(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ArrayWithKeys(VisitArrayAbstrata):
  def _init_(self, exps):
    self.exps = exps
  def accept(self, visitor):
    return visitor.visitArrayWithKeys(self)

#Corrigir isto aqui não sei como fica olhar o visitor
#class VisitArrayKeys(VisitArrayAbstrata):
#  def _init_(self, id, exps):
#    self.id = id
#    self.exp = exps
#  def accept(self, visitor):
#    return visitor.visitArrayKeys(self)

class ArrayDecl(VisitArrayAbstrata):
  def _init_(self, id, exp):
    self.id = id
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitArray_decl(self)

class ArrayDeclSimple(VisitArrayAbstrata):
  def _init_(self, id):
    self.id = id
  def accept(self, visitor):
    return visitor.visitArray_declSimple(self)

class ExpAbstrata(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class OrExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitOrExp(self)

class AndExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitAndExp(self)

class LessThanExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitLessThanExp(self)

class BiggerThanExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitBiggerThanExp(self)

class LessEqualExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitLessEqualExp(self)

class BiggerEqualExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitBiggerEqualExp(self)

class DifExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitDifExp(self)

class EqualExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitEqualExp(self)

class BitwiseExecOrExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitBitwiseExecOrExp(self)

class BitwiseAndExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitBitwiseAndExp(self)

class ConcatenationExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitConcatenationExp(self)

class SumExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitSumExp(self)

class ModuleExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitModuleExp(self)

class DivExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitDivExp(self)

class DivIntExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitDivIntExp(self)

class MultExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitMultExp(self)

class NotExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitNotExp(self)

class DenialExp(VisitExpAbstrata):
  def _init_(self, exp)
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitDenialExp(self)

class UnaryBitwiseNotExp(VisitExpAbstrata):
  def _init_(self, exp)
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitUnaryBitwiseNotExp(self)

class PowExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitPowExp(self)

class DotExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitDotExp(self)

class NumberExp(VisitExpAbstrata):
  def _init_(self, value)
    self.value = value
  def accept(self, visitor):
    return visitor.visitNumberExp(self)

class StringExp(VisitExpAbstrata):
  def _init_(self, stringValue)
    self.stringValue = stringValue
  def accept(self, visitor):
    return visitor.visitStringExp(self)

class IdExp(VisitExpAbstrata):
  def _init_(self, id)
    self.id = id
  def accept(self, visitor):
    return visitor.visitIdExp(self)

class LocalIdExp(VisitExpAbstrata):
  def _init_(self, localId)
    self.localId = localId
  def accept(self, visitor):
    return visitor.visitLocalIdExp(self)

class TrueExp(VisitExpAbstrata):
  def _init_(self, trueExp)
    self.trueExp = trueExp
  def accept(self, visitor):
    return visitor.visitTrueExp(self)

class FalseExp(VisitExpAbstrata):
  def _init_(self, falseExp)
    self.falseExp = falseExp
  def accept(self, visitor):
    return visitor.visitTrueExp(self)

class BitwiseOrExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitBitwiseOrExp(self)

class SubExp(VisitExpAbstrata):
  def _init_(self, exp1, exp2)
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitSubExp(self)

class LenghtExp(VisitExpAbstrata):
  def _init_(self, exp)
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitLenghtExp(self)