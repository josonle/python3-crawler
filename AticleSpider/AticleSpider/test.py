def yield_test():
    for i in range(5):
        yield call(i)
        print("i=", i)
        # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    return i * 2


# 使用for循环
for i in yield_test():
    print(i, ",")
