"""
file_write.py 写函数示例
"""

# 打开文件

# 写操作
# f = open('file', 'w')  # 清空
# f.write("hello 死鬼\n")
# f.write("哎呀，干啥\n")

# f = open('file','ab')  # 续写
# f.write("hello 死鬼\n".encode())
# f.write("哎呀，干啥\n".encode())

# writelines,换行自己加换行符
f = open('file','w')
f.writelines(['abc\n','你好\n','北京\n'])

f.close()
