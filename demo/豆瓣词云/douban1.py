import requests
import os
import re
import time
import random
import jieba



#生成SESSION对象，用于保存Cookie
s = requests.Session()

def login_douban():
    '''创建登录url'''
    login_url = "https://accounts.douban.com/j/mobile/login/basic"
    #创建请求头文件
    headers = {'User-Agent':'Mozilla/5.0','Referer':'https://accounts.douban.com/passport/login_popup?login_source=anony'}
    #传递用户名和密码
    data = {
        'name': '18829292236',
        'password': 'c151602',
        'remember': 'false'
    }
    # 解决异常
    try:
        r = s.post(login_url, headers=headers, data=data)
        r.raise_for_status()
    except:
        print("爬取失败")

    # 打印请求结果
    print("---123---/n")
    print(r.text+"/n")
    print("---456---/n")





def spider_comment(start=0):
    '''
    爬取某页影评
    :param start:起始位置，相当于分页参数
    :return:
    '''
    #制作请求URL
    comment_url = "https://movie.douban.com/subject/26266893/comments?start=%s&limit=20&sort=new_score&status=P"%start
    #制作请求头
    headers = {'user-agent':'Mozilla/5.0'}
    try:
        #请求状态
        r = s.get(comment_url,headers=headers)
        #print(r)
        r.raise_for_status()
    except:
        print("爬取请求失败，start="+start)

    #找到影评的位置
    #global comments
    comments = re.findall('<span class="short">(.*)</span>',r.text)

    with open("douban.txt",'a+',encoding='utf-8') as file:
        file.writelines('\n'.join(comments))
        #file.write(r.text)


def batch_spider_comment():
    #写入数据前清空文件中的数据
    if os.path.exists("douban.txt"):
        os.remove("douban.txt")

    start=0
    #爬取20页数据
    while start<1:
        spider_comment(start)
        #print("===============")
        start+=1
        print("---正在爬取第%s页---"%start)
        time.sleep(random.random()*3)

    print("爬取完毕")


def cut_word():
    '''使用结巴分词'''
    with open("douban.txt",encoding="UTF-8") as file:
        comment_txt = file.read()
        wordlist = jieba.cut(comment_txt,cut_all=True)
        wl=" ".join(wordlist)
        print(wl)
        return wl



if __name__ == '__main__':
    #login_douban()
    #spider_comment()
    batch_spider_comment()
    cut_word()

