# 将lam包的目录引入环境变量

import sys
from pathlib import Path
lampy_dir = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(lampy_dir))

