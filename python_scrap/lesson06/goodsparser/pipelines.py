# -*- coding: utf-8 -*-

import base64

import scrapy
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline


class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['images']:
            for img in item['images']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            images = [itm[1] for itm in results if itm[0]]
            binary = []
            for image in images:
                with open(image, "rb") as imageFile:
                    binary.append(base64.b64encode(imageFile.read()))
            item['images'] = binary
        return item


class MongoPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.youla

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        collection.update_one({'_id': item['url']}, {'$set': item}, upsert=True)
        return item
