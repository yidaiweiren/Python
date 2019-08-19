import requests

#生成SESSION对象，用于保存Cookie
s = requests.Session()

def login_douban():

    '''创建登录url'''
    login_url = "https://accounts.douban.com/j/mobile/login/basic"

    #创建请求头文件
    headers = {'User-Agent':'Mozilla/5.0','Referer':'https://accounts.douban.com/passport/login_popup?login_source=anony'}

    #传递用户名和密码
    data = {

        'name':'18829292236',
        'password':'c151602',
        'remember':'false'
    }

    #解决异常
    try:
        r = s.post(login_url,headers=headers,data=data)
        r.raise_for_status()
    except:
        print("爬取失败")

    #打印请求结果
    print(r.text)

if __name__ == '__main__':
    login_douban()

