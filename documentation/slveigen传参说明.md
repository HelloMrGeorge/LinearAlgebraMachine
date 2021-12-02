slveigenvalue(a:str):#特征值
 slveigengetcharpoly(a:str):#特征多项式
传回的参数为json格式需要使用json.loads


slveigenvectors(a:str):#特征向量
传回参数为list
需要取出元素使用具体为：
eigenvectors[i]为第i个特征值的特征向量列表
eigenvectors[i][0]:第i个特征值
eigenvectors[i][1]:重数
eigenvectors[i][2][j]:特征向量对应列表()



slveigenCourse(a:str):#（特征值求解过程）
返回参数为字典含有关键字
'matrix'：对应原矩阵使用p['matrix']取出
'eigenvectors'    使用eigenvectors=p['eigenvectors']取出后对应slveigenvectors(a:str)操作，见上述内容
'charpoly'对应    特征多项式使用p['charpoly']取出
'lambdamat'      对应矩阵得到矩阵λE-A 使用p['lambdamat']
'lambdamatvalue'    对应第i个特征值的矩阵使用p['lambdamatvalue'][i]取出



