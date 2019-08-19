'''

filter():对指定序列执行过滤操作
执行完成后返回的结果：true//false
python中：“0代表false”，“1代表true”
如果给filter（过滤条件，需要过滤的东西）的过滤条件为None，代表不过滤
'''

ret = filter(lambda x:x%2,[1,2,3,4,5])
for tmp in ret:
    print(tmp)



