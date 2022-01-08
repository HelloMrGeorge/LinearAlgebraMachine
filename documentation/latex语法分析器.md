# LaTeX语法分析器

Source: latexparser

> 请在根目录新建latexparser库以完成任务，不要引用lam库的功能防止交叉引用。

## 需求概述

---

latex语法分析器需要提供一个接口，接收`str`类型的参数，返回`sympy.MutableDenseMatrix`类型的对象。因为前端发送的数据到目前为止总是矩阵形式的文本，如

> `[[1, 2, 3], [3.3, 5.2, 1.3], [7, 11, 32]]`

所以需要矩阵形式的返回值，故建议使用`sympy.MutableDenseMatrix`作为返回值。返回的矩阵的每个元素都应属于sympy库当中的类型，这些元素对应着输入的文本参数的每个单元。对于之前举的例子，它每个单元对应的类型就是(省略sympy前缀)

> `[[Integer, Integer, Integer], [Float, Float, Float], [Integer, Integer, Integer]]`

这个例子，并没有涉及任何latex命令，详细的每个数学元素与sympy类型对应关系可以参考后面的类型对照表，注意latex命令的反斜杠字符，如`\sqrt`，请不要变成转义字符。

此外除了一般形式的矩阵文本，latex语法分析器也应支持解析latex语法的矩阵文本(`\left[\begin{matrix} ... \end{matrix}\right]`)，仍然用第一个例子，它的latex语法是

> `\left[\begin{matrix} 1 & 2 & 3 \\3.3 & 5.2 & 1.3 \\7 & 11 & 32 \end{matrix}\right]`

如果前端发送的latex矩阵形式的文本，那么接口也应返回相应的`MutableDenseMatrix`对象。


## 类型对照表

---

类型一栏均省略了sympy的前缀，具体内容请查询sympy文档

| 数学元素 | 示例 | 类型 | 备注 |
| --- | --- | --- | --- |
| 整数 | 10 | Integer | 纯数字文本 |
| 小数 | 10.1 | Float | 纯数字文本 |
| 拉丁字母 | a | Symbol | 不要用Symbol的构造函数创建，而是用sympy.abc的内建对象创建，它已经内置了所有拉丁和希腊字母
| 希腊字母 | \epsilon | Symbol | 用sympy.abc的内建对象创建，示例对应的内建对象是sympy.abc.epsilon
| 加法 | a+b | Add | 加法需要兼容字母运算 |
| 减法 | a-b | Add | a减b视为加-b |
| 乘法 | ab | Mul | 乘法需要兼容字母运算 |
| 乘方 | a^{b} | Pow | 乘方需要兼容字母运算, 当指数只有一个字符可以省略大括号，如a^b |
| 分式 | \frac{a}{b} | Mul | a除以b视为乘b^{-1}，故用Mul类型 |
| 根式 | \sqrt{a} | Pow | 开方视为1/2次幂 |

除了以上提到的内容，显然还有对数，三角函数等数学元素，我们分阶段实现，这些内容可以放到后面拓展。

