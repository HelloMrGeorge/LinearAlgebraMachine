import numpy as np
from lam.core import core, interpreter, gausselim


a = '1,1,2;1,3,4;2,3,4'
a = interpreter.interpret(a)
b = gausselim.gaussElim(a)
b.print()