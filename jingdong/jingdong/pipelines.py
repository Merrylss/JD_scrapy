# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class JingdongPipeline(object):
    def process_item(self, item, spider):
        return item


class MyPipeline(object):

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user='root',
            password='123456',
            database='jingdong',
            charset='utf8'
        )

        self.my_sql = self.conn.cursor()

    def process_item(self, item, spider):

        name = item['title']
        # 价格
        price = item['price']
        # 链接
        url = item['url']
        # 评论
        comment = item['comment_num']
        # 店铺
        info = item['info']

        sql = 'insert into info2 (`name`, `price`, `url`, `comment`, `info`) values ("%s","%s","%s","%s","%s")'

        self.my_sql.execute(sql % (name, price, url, comment, info))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.my_sql.close()
        self.conn.close()