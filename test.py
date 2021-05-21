import requests

class jdcomment_spider():
    def __init__(self,file_name='jidong_pinglun'):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }
        #打开文件
        self.fp = open(f'./{file_name}.txt','w',encoding='utf-8')


    def parse_one_page(self):
        # 指定url
        url = 'https://club.jd.com/comment/productPageComments.action?productId=10024696984098&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }

        # 发起请求
        response = requests.get(url, headers=self.headers)
        print(response)

        # 将json格式的字符串转化为字典
        js_date = response.json()

        # 提取数据
        comment_list = js_date['comments']
        print(comment_list)
        # for comment in comment_list:
        #     # 昵称
        #     nickname = comment.get("nickname")
        #     goods_id = comment.get("id")
        #     score = comment.get("score")

            #存储数据
            # self.fp.write(f'{nickname}\t{goods_id}\t{score}')

jd = jdcomment_spider()
jd.parse_one_page()