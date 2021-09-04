from typing import List
import numpy as np
from lam.core import ndmatrix, gelim, input, output
from lam.det import det

a = '1,1,2;1,3,4;2,3,4'
a = input.interpret(a)
# pr = det.laplaceExpand(a, 1)
# print(pr[0])

step = output.MatAlgStep()
step.appendDic('+', 2, a)
process = output.Process()
process.append(step)
det.laplaceDet(process)
for i in process:
    print(i)
