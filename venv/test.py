import requests
from lxml import etree
#解析xml解析器--网页下载下来是字符串形式，使用etree来重新构建节点树
from bs4 import BeautifulSoup
#BeautifulSoup解析器--直译：美味的汤。非常灵活
#
with open("123.txt","a",encoding="utf-8") as f:
#将as前的‘获取的值’赋值给as后面的变量
    for i in range(10):
    #range 定义循环遍历的最大值--范围
        url="https://music.douban.com/top250?start={}".format(i*25)
        headers={"User_Agent":"Mozilla/5.0(compatible;MSIE 5.5;Windows 10)"}
        data=requests.get(url,headers=headers).text
        #user_Agent构造
        #url=...
        #user_agent=...
        #headers={'User_Agent':user_agent}
        #req=requests.request(url=url,headers=headers)
        #chrome浏览器
        #user_agent='Mozilla/5.0(compatible;MSIE 5.5;Windows 10)'
        s=etree.HTML(data)
        #etree.HTML(data)
        #调用html类来对下载下来的html文件进行初始化。成功构建xpath解析对象，同时自动修正html文档
        musics=s.xpath('//*[@id="content"]/div/div[1]/div/table')
        #‘//*’选取文档中的所有元素
        #‘@’属性的意思
        for music in musics:
            music_name=music.xpath('./tr/td[2]/div/a/text()')[0].strip()
            music_author=music.xpath('./tr/td[2]/div/p[1]/text()')[0].strip()
            music_pingfen=music.xpath('./tr/td[2]/div/div/span[2]/text()')[0].strip()
            #music_pingjia=music.xpath('./tr/td[2]/div/div/span[3]/text()')[0].strip()
            f.write("歌名:{}\n".format(music_name))
            #将music_name获取到的值写入"歌名:{获取到的值}\n"这个接收参数中，并换行
            f.write("作者:{}\n".format(music_author))
            f.write("评分:{}\n".format(music_pingfen))
            #f.write("评价:{}\n".format(music_pingjia))
            f.write("\n")