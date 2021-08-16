from package.core import gausselim,core

a = '1,1,1,1;1,3,4,1;0,4,5,1'
b = core.interpret(a)
c = gausselim.gaussElim(b)
for i in c:
    print(i)

