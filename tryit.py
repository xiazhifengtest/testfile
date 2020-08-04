try:
    fh = open("e111111111111tstfile", "w")
    fh.write("这是一个testfile，用于测试异常")
except IOError:
    print("error:没有找到活读取到文件")
else:
    print("内容写入文件成功")
    fh.close()

a = ['one', 'two', 'three']
for i in a[::-1]:
    print(i)

print(list(range(100, 200)))

b = list(range(101, 200))
print(b)
