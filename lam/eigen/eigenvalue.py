import sympy as sp


class EigenSolver:

    def __init__(self, mat: sp.MutableDenseMatrix) -> None:
        self.mat: sp.MutableDenseMatrix = mat
        self.lambdamat:sp.MutableDenseMatrix = None#求解过程中的矩阵（λE-A）
        self.lambdamat_value:list = None #求解过程中的λiE-A构成的列表
        self.charploy: sp.Poly = None    #Poly.all_coeffs()可以获取系数列表
        self.eigenvalues: dict = None   #特征值字段是一个字典，键代表特征值，值代表对应的重数
        self.eigenvectors: list = None  #特征向量字段的数据已经包含了特征值

    def getCharpoly(self, simplify = sp.simplify):
        self.charploy = getCharpoly(self.mat, simplify = simplify)
        return self.charploy
    def getlambdamat(self):
        self.lambdamat=getlambdamat(self.mat)
        return self.lambdamat
    def getlambdamatvalue(self):
        self.lambdamat_value=getlambdamatvalue(self.mat)
        return self.lambdamat_value
    def getEigenvalues(self, error_when_incomplete=True, **flags):
        self.eigenvalues = getEigenvalues(self.mat, error_when_incomplete=error_when_incomplete, **flags)
        return self.eigenvalues

    def getEigenvectors(self, error_when_incomplete=True, **flags):
        self.eigenvectors = getEigenvectors(self.mat, error_when_incomplete=error_when_incomplete, **flags)
        return self.eigenvectors

    def get_course(self):
        return {"matrix": self.mat, "lambdamat":self.getlambdamat(),"lambdamatvalue":self.getlambdamatvalue(),"charpoly": self.getCharpoly(), "eigenvectors": self.getEigenvectors()}

def getCharpoly(mat: sp.MutableDenseMatrix, simplify = sp.simplify) -> sp.PurePoly:
    #封装了sympy的charpoly()方法，请不要在矩阵中加入含lambda的变量，因为默认特征多项式的自变量的是lambda
    return mat.charpoly(simplify = simplify)
def getlambdamat(mat: sp.MutableDenseMatrix, error_when_incomplete=True, **flags):
    lambdamatrix = -mat
    lambdamatrix1 = sp.eye(mat.shape[0])
    x = sp.symbols("lambda")
    lambdamatrix1 = lambdamatrix1 * x
    lambdamatrix = lambdamatrix + lambdamatrix1
    return lambdamatrix
def getlambdamatvalue(mat: sp.MutableDenseMatrix, error_when_incomplete=True, **flags):
    lambdamatrix = -mat
    lambdamatrix1 = sp.eye(mat.shape[0])
    eigenvalues=list(mat.eigenvals().keys())
    list0=[]
    for i in range(len(eigenvalues)):
        lambdamatrix2=lambdamatrix1*eigenvalues[i]
        lambdamatrix3 = lambdamatrix + lambdamatrix2
        list0.append(lambdamatrix3)
    return list0
def getEigenvalues(mat: sp.MutableDenseMatrix, error_when_incomplete=True, **flags):
    return mat.eigenvals(error_when_incomplete=error_when_incomplete, **flags)

def getEigenvectors(mat: sp.MutableDenseMatrix, error_when_incomplete=True, **flags):
    return mat.eigenvects(error_when_incomplete=error_when_incomplete, **flags)

if __name__ == "__main__":
    mat = sp.Matrix(3, 3, [5, 6, -3, -1, 0, 1, 1, 2, -1])
    eigenSolver = EigenSolver(mat)
    p1 = eigenSolver.getCharpoly()
    p2: dict = eigenSolver.getEigenvalues()
    p3 = eigenSolver.getEigenvectors()
    p4=eigenSolver.get_course()
    p5=eigenSolver.getlambdamatvalue()
    print(sp.latex(p4['charpoly']))
    print(p4['charpoly'])
