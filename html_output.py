import pymysql

class HtmlOutPut:
    def __init__(self):
        self.datas = []  # 存放搜集的数据

    def collect_data(self, new_data):
        if (new_data is None):
            return
        self.datas.append(new_data)

    def output_html(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='Spiderdata',
                               charset='utf8')
        conn.autocommit(False)
        cursor = conn.cursor()
        for data in self.datas:
            #print(data['summary'])
            sqlinsert = "insert into items(url,title,summary) values('%s','%s','%s')" % (data['url'], data['title'], data['summary'])
            try:
                cursor.execute(sqlinsert)
                #print(cursor.rowcount)
                conn.commit()
            except Exception as e:
                print("error:" + str(e))
        conn.close()


