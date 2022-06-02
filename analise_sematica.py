from Abstract_Visitor import AbstractVisitor
import SymbolTable as st
from Visitor import Visitor


import Sintaxe_Abstrata as sa

class SemanticVisitor(AbstractVisitor):
  def __init__(self):
        self.printer = Visitor()
        st.beginScope('main')

  def visitFucntion(self, function):
    function.signature.accept(self)
    function.comands.accept(self)

  def visitLocalFunction(self, localFunction):
    localFunction.signature.accept(self)
    localFunction.comands.accept(self)

    