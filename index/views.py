from django.shortcuts import render
from django.http import HttpResponse
from django.db.models  import F,Q
from index.models import Author,Count
from django.db import transaction,IntegrityError,DatabaseError
from datetime import datetime
from django.views.decorators.cache import cache_page
from SSHLog.MLog import mlog as VLog


@cache_page(60*15)
def about_views(request):
    return render(request, 'about.html')

# 开启事务
@transaction.atomic
def add_author_views(request):
    # 自动提交
    # Author.objects.create(name=u'wangbaoqiang',age=33,email='wangbaoqiang@qqq.com')

    # 断点回滚
    author_name = u'linghuchong'
    author = Author(name=author_name, age=24, email='linghuchong@qqq.com')
    author.save()
     # transaction now contains author.save()

    sid = transaction.savepoint()

    try:
        count = Count(name=author_name, article_amount=1)
        count.save()
        # transaction now contains author.save() and count.save()
        transaction.savepoint_commit(sid)
        # open transaction still contains author.save() and count.save()
    except IntegrityError:
        transaction.savepoint_rollback(sid)
        # open transaction now contains only count.save()
        # 保存author操作回滚后，事务只剩下一个操作

    # 整体回滚
    # author_name = u'renyingying'
    # author = Author(name=author_name, age=24, email='renyingying@qqq.com')
    # # author.save()
    #
    # count = Count(name=author_name, article_amount=1)
    # count.save()
    #
    # try:
    #     with transaction.atomic():
    #         author.save()
    #         #count.save()
    #         #raise DatabaseError
    # except DatabaseError:     # 自动回滚
    #         pass

    return HttpResponse('Add OK')


def get_author_views(request):
    authors = Author.objects.all()
    return render(request, 'show_authors.html', locals())


def select_views(request):
    if request.method == 'GET':
        return render(request, 'selectWebsite.html')
    else:
        option = request.form['option']


def add_secondHouse_msg(request):
    if request.method == 'GET':

        from SHHData.saveLianjiaDatas import saveDatas

        IsSaveDatas = saveDatas('https://gz.lianjia.com/zufang/tianhe/rt200600000002/')

        if IsSaveDatas == 1:
        # if False:
            resultMsg = '爬虫数据存储成功！'
            return render(request, 'saveDataRes.html', {'msg': resultMsg})
        else:
            resultMsg = '爬虫数据存储失败~'
            return render(request, 'saveDataRes.html', {'msg': resultMsg})
    else:
        pass






