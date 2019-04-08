from django.db import models
from mongoengine import *
from datetime import datetime



# 映射到数据库
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    website = models.URLField()  # 映射到数据库中是固定字符串


class Author(models.Model):
    name = models.CharField(max_length=30,null=False)
    age = models.IntegerField()
    email = models.URLField(null=True)


class Book(models.Model):
    title = models.CharField(max_length=50)
    publicatiion_date =  models.DateField(default=datetime.now())


class Count(models.Model):
    name = models.CharField(max_length=30)
    article_amount = models.IntegerField()


connect('secondHandHouse')  # 显示连接数据库，必须有
class SecondHouse(Document):
    meta = {
        'collection': 'secondHandHouseMsg'
    }
    house_id = SequenceField(required=True, primary_key=True)
    house_name = StringField(max_length=50)
    house_floor = StringField(max_length=5)
    house_area = FloatField(max_length=5)
    house_layout = StringField(max_length=20)  # 房间布局
    house_pay = FloatField(max_length=5)
    house_region = DictField()
    house_subway = DictField()
    house_furnitures = ListField()
    msg_update_time = DateTimeField(default=datetime.now())  # 注意不是DateField(否则只存日期)

    # EmbeddedDocumentField 正确使用：ListField内部嵌套，如存储文章评论
    # ListField(EmbeddedDocumentField(Region))

    # 默认搜索条件
    @queryset_manager
    def objects(doc_cls, queryset):
        return queryset.order_by('-msg_update_time')


# class Region(EmbeddedDocument):
#     city = StringField(max_length=10)
#     district = StringField(max_length=10)
#     community = StringField(max_length=10)
#
# class Subway(EmbeddedDocument):
#     line = IntField(max_length=5)
#     distance = StringField(max_length=5)
