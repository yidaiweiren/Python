def test1():
    print ("-----test1-----")
def test2():
    print ("-----test2-----")

print (__name__)
#__name__自己执行，显示的是__main__,别人调用执行，显示的是sendmsg（模块名）

if __name__ == "__main__":
    test1()
    test2()