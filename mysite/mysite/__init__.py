import sys
# 增加顶级目录到环境变量
from pathlib import Path
lampy_dir = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(lampy_dir))

# 集成语法分析器
from latex import parser
matParser = parser.matParser
from sympy.parsing.latex import parse_latex
exprParser = parse_latex




