"""
with语句演示
"""

with open('file') as f:  # 生成对象
    data = f.read()
    print(data)

# 语句块结束自动销毁f
