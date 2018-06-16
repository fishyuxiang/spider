import spider_main

from tkinter import *
import tkinter.messagebox as messagebox
import pymysql

class GuiDisplay(Frame):#构造图形界面
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.buttonspider = Button(self, text='爬取数据', command=self.spider)#爬取数据按钮
        self.buttonspider.pack()
        self.buttonshow = Button(self, text='展示数据', command=self.show)#展示数据按钮
        self.buttonshow.pack()
        self.result_text = Text(self.master, width=150, height=70)#通过文本显示
        self.result_text.pack()

    def spider(self):#爬取数据，存入mysql数据库
        root_url = "http://baike.baidu.com/item/Python"
        obj_spider = spider_main.spiderMain()
        obj_spider.craw(root_url)
        messagebox.showinfo('Message', 'success!')

    def show(self):#从数据库读取数据并展示
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='Spiderdata',
                                   charset='utf8')
        conn.autocommit(False)
        cursor = conn.cursor()
        sql = "select * from items"
        cursor.execute(sql)

        results = cursor.fetchall()
        for row in results:
            self.result_text.insert(INSERT, row[0] + '\n')
            self.result_text.insert(INSERT, '\n')
            self.result_text.insert(INSERT, row[1] + '\n')
            self.result_text.insert(INSERT, row[2] + '\n')
            self.result_text.insert(INSERT, '\n')
        conn.close()

 # 创建main方法

if __name__ == "__main__":
    app = GuiDisplay()
    app.master.title('爬虫程序')
    app.master.geometry('1000x680+10+10')
    app.master["bg"]="pink"
    app.mainloop()