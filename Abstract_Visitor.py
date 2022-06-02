from abc import abstractmethod
from abc import ABCMeta

# O QUE JÁ FOI FEITO
#visitProgram
#function
#signature
#compoundComand
#singleComand
#comandReturn

#DEFINIÇÕES DE EXPRESSÕES (O QUE JPA FOI FEITO)
#visitOrExp .
#visitAndExp.
#visitLessThanExp.
#visitBiggerThanExp.
#visitLessEqualExp.
#visitBiggerEqualExp.
#visitDifExp.
#visitEqualExp.
#visitBitwiseExecOrExp.
# FALTA O BITWISE OR SOZINHO, EXP 9 //não falta mais
#visitBitwiseAndExp.
#visitConcatenationExp.
#FALTA O BITWISE SUB, EXP14 //não falta mais
#visitSumExp.
#visitModuleExp.
#visitDivExp.
#visitDivIntExp.
#visitMultExp.
#visitNotExp.
#visitDenialExp.
#visitUnaryBitwiseNotExp.
#FALTA LENGHT, EXP 22 \\não falta mais 
#visitPowExp.
#visitDotExp.
#visitNumberExp.
#//t_LENGHT = r'\#'
#visitStringExp
#visitIdExp
#visitLocalIdExp
#visitTrueExp
#visitFalseExp




class AbstractVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visitorProgram(self, program):
        pass

    @abstractmethod
    def visitorFunction(self, functionDecl):
        pass

    @abstractmethod
    def visitorLocalFunction(self, local_functionDecl):
        pass

    @abstractmethod
    def visitorSignature(self, signatureDecl):
        pass

    @abstractmethod
    def visitorSingleSigParam(self, singleSigParam):
        pass

    @abstractmethod
    def visitorCompoundSigParam(self, compoundSigParam):
        pass

    @abstractmethod
    def visitorComands(self, comands):
        pass

    @abstractmethod
    def visitorSigleComand(self, SingleComand):
        pass

    @abstractmethod
    def visitorCompoundComand(self, CompoundComand):
        pass

    @abstractmethod
    def visitorComandIf(self, comandIf):
        pass

    @abstractmethod
    def visitorComandElseIf(self, comandElseIf):
        pass
      
    @abstractmethod
    def visitorOtherComand(self,otherComand):
      pass
    @abstractmethod
    def visitorComandForDo(self, comandForDo):
        pass

    @abstractmethod
    def visitorComandForIn(self, comandForIn):
        pass

    @abstractmethod
    def visitorComandWhile(self, comandWhile):
        pass

    @abstractmethod
    def visitorComandReturn(self, comandReturn):
        pass

    @abstractmethod
    def visitorListExp(self, list_exp):
        pass

    @abstractmethod
    def visitorCall(self, call):
        pass

    @abstractmethod
    def visitorArray(self, array):
        pass

    @abstractmethod
    def visitorComandExp(self, ComandExp):
        pass

    @abstractmethod
    def visitorCallExp(self, callExp):
        pass

    @abstractmethod
    def visitorOrExp(self, orExp):
        pass

    @abstractmethod
    def visitorAndExp(self, andExp):
        pass

    @abstractmethod
    def visitorLessThanExp(self, lessThanExp):
        pass

    @abstractmethod
    def visitorBiggerThanExp(self, biggerThanExp):
        pass

    @abstractmethod
    def visitorLessEqualExp(self, lessEqualExp):
        pass

    @abstractmethod
    def visitorBiggerEqualExp(self, biggerEqualExp):
        pass

    @abstractmethod
    def visitorDifExp(self, difExp):
        pass

    @abstractmethod
    def visitorEqualExp(self, equalExp):
        pass

    @abstractmethod
    def visitorBitwiseOrExp(self, bitwiseOrExp):
        pass

    @abstractmethod
    def visitorBitwiseExecOrExp(self, bitwiseExecOrExp):
        pass

    @abstractmethod
    def visitorBitwiseAndExp(self, bitwiseAndExp):
        pass

    @abstractmethod
    def visitorConcatenationExp(self, concatenationExp):
        pass

    @abstractmethod
    def visitorSubExp(self, subExp):
        pass

    @abstractmethod
    def visitorSumExp(self, sumExp):
        pass

    @abstractmethod
    def visitorModuleExp(self, moduleExp):
        pass

    @abstractmethod
    def visitorDivExp(self, divExp):
        pass

    @abstractmethod
    def visitorDivIntExp(self, divIntExp):
        pass

    @abstractmethod
    def visitorMultExp(self, mulExp):
        pass

    @abstractmethod
    def visitorNotExp(self, notExp):
        pass

    @abstractmethod
    def visitorDenialExp(self, denialExp):
        pass

    @abstractmethod
    def visitorUnaryBitwiseNotExp(self, unaryBitwiseNotExp):
        pass

    @abstractmethod
    def visitorPowExp(self, powExp):
        pass

    @abstractmethod
    def visitorDotExp(self, dotExp):
        pass

    @abstractmethod
    def visitorNumberExp(self, numberExp):
        pass

    @abstractmethod
    def visitorStringExp(self, stringExp):
        pass

    @abstractmethod
    def visitorIdExp(self, idExp):
        pass

    @abstractmethod
    def visitorLocalIdExp(self, localIdExp):
        pass

    @abstractmethod
    def visitorTrueExp(self, trueExp):
        pass

    @abstractmethod
    def visitorFalseExp(self, falseExp):
        pass

  