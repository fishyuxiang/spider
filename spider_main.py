# 创建类
import url_manager, html_downloader, html_output, html_parser

class spiderMain:
    # 构造函数 初始化
    def __init__(self):
        # 实例化需引用的对象
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.output = html_output.HtmlOutPut()
        self.parser = html_parser.HtmlParser()

    def craw(self, root_url):
        # 添加一个到url中
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                # 下载
                html_context = self.downloader.downloade(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_context)
                print(new_urls)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                # 爬一千多个界面
                if (count == 1050):
                    break
                count += 1
            except Exception as e:
                print("craw faile!  error: " +str(e))
        self.output.output_html()


