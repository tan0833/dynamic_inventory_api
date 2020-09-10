import random
from random_words import RandomWords

class CreateRandom:

    def random_create_char(self):
        '''
        随机生成汉字，包括生僻字
        :return:
        '''
        char_one = chr(random.randint(0x4e00, 0x9fbf)) + chr(random.randint(0x4e00, 0x9fbf))
        return char_one

    def random_create_letter(self):
        '''
        随机生成字母
        :return:
        '''
        H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        letter = ''
        for i in range(10):
            letter = letter + random.choice(H)
        return letter

    def random_create_symbol(self):
        '''
        随机生成特殊符号
        :return:
        '''
        symbol_name = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '[', '}',
                       ']', ':', ';', '"', '\,', '|',
                       ' ·@*|', '<', ',', '.', '>', '?', '/', ' ']
        symbol = random.choice(symbol_name)
        return symbol

    def random_create_digit(self):
        '''
        创建随机数字
        :return:
        '''
        return random.randint(0, 99)


    def gbk2312(self):
        '''
        随机生成汉字
        :return:
        '''
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x}{body:x}'
        str = bytes.fromhex(val).decode('gb2312')
        return str

    def random_create_company(self):
        '''
        随机创建公司
        :return:
        '''

        cities_name = ["成都", "武汉", "南京", "杭州", "北京", "广州", "上海", "西安", "天津", "沈阳", "宁波", "深圳", "郑州", "南宁", "长沙", "哈尔滨",
                       "台北", "厦门", "宁波",
                       "成都武侯区", "成都金牛区", "成都成华区", "成都高新区", "成都青羊区", "锦江区", "成都郫县", "高新西区", "宜宾", "内江", "眉山", "合肥",
                       "马鞍山", "桂林","兰州", "乌鲁木齐", "鄂尔多斯", "呼和浩特", "太原", "大同", "运城", "驻马店", "台州", "西宁", "日喀则",
                       "温州", "自贡", "保定", "商丘", "石河子", "喀什", "库尔勒", "宜昌", "荆州", "周口", "齐齐哈尔"
                       ]
        compellation = ["下单", "查单", "运输", "库存", "采购", "销售", "服务", "测试", "搜索", "物流", "交通", "服务"]
        company_type = ["有限公司", "服务有限公司", "责任有限公司", "贸易有限公司", "咨询有限公司", "厂", "经营部", "集团有限公司", "集团"]

        company_name = random.choice(cities_name) + self.gbk2312() + self.gbk2312() + random.choice(compellation) + random.choice(company_type)
        return company_name


    def random_create_mobile_phone(self):
        '''
        随机创建手机号码
        :return:
        '''
        num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187',
                     '188','147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189','199']
        phone_num = random.choice(num_start) + str(random.randint(10000000,99999999))
        return phone_num

    def random_create_word(self):
        '''
        随机生成单词
        :return:
        '''
        lower_letter='abcdefghilmnoprstvw'
        rw = RandomWords()
        random_letter = random.choice(lower_letter)
        words = rw.random_words(letter=random_letter, count=50)
        word = random.choice(words)
        return word

    def random_create_english_company(self):
        '''
        随机生成英文公司名称
        :return:
        '''
        company_suffix = ['Co.Ltd.','Corp.','S.A.','GmbH','BHD','SDN','S.A.R.L','B.V.N.V','AG','S.A.','S.P.A.','S.R.L.','PLC','AB','OY']
        word1 = self.random_create_word().capitalize()
        word2 = self.random_create_word().capitalize()
        word3 = self.random_create_word().capitalize()
        english_company_name = word1 + ' ' + word2 + ' ' + word3 + ' '+  random.choice(company_suffix)
        return english_company_name

    def random_create_email(self):
        '''
        随机生成邮箱
        :return:
        '''
        email_suffix = ['@189.com','@qq.com','@126.com','@163.com','@inc.com','@aa.com']
        letter = self.random_create_letter()
        email_name = letter + random.choice(email_suffix)
        return email_name


if __name__ == '__main__':
        t = CreateRandom()
        a = t.random_create_email()
        print(a)