
'''
在__getattribute__方法中禁止使用self.xx
在__getattribute__方法中禁止使用self.xx
在__getattribute__方法中禁止使用self.xx
在__getattribute__方法中禁止使用self.xx
'''
class Person(object):
    def __getattribute__(self,obj):
        print("-----test-----")
        if obj.startswith("a"):
            return "haha"
        else:
            return self.test

    def test(self):
        print("heihei")


t = Person()
print(t.a)
print(t.b)

