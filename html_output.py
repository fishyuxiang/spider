class HtmlOutPut:
    def __init__(self):
        self.datas = []  # 存放搜集的数据

    def collect_data(self, new_data):
        if (new_data is None):
            return
        self.datas.append(new_data)

    def output_html(self):
        fout = open('output.log', 'w', encoding='utf8')  # 写入文件 防止中文乱码

        for data in self.datas:

            fout.write('%s\n' % data['url'])
            fout.write('%s\n' % data['title'])
            fout.write('%s\n' % data['summary'])
            fout.write('\n')

        fout.close()