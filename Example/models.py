from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'姓名', default='')
    sex = models.IntegerField(default=1)
    age = models.IntegerField(null=True, default=30, blank=True)
    tel = models.CharField(max_length=50, null=True, unique=False, default='')
    passwd = models.CharField(max_length=100, default='', null=True)
    qq = models.CharField(max_length=20, null=True, default='')
    weixin = models.CharField(max_length=30, null=True, default='')
    e_mail = models.CharField(max_length=50, null=True, default='')
    title = models.TextField(verbose_name=u'头衔', null=True, default='', blank=True)
    image = models.CharField(max_length=255, null=True, default='', verbose_name=u'头像')
    company = models.CharField(max_length=100, null=True, default='', verbose_name=u'公司名称')
    com_addr = models.CharField(max_length=300, null=True, default='', verbose_name=u'公司地址')
    com_type = models.CharField(default='', verbose_name=u'公司类型', max_length=300)

    class Meta:
        db_table = 'customer'




class NewsCategory(models.Model):
    """新闻分类"""
    
    category_name = models.CharField(verbose_name="分类名称", null=True, max_length=30)
    deleted = models.BooleanField(verbose_name='是否删除', default=False)
    create_time = models.DateTimeField(verbose_name='创建时间', null=True, auto_now_add=True)

    class Meta:
        db_table = 'news_category'
        verbose_name_plural = '新闻分类'

    def __unicode__(self):
        return self.category_name

class WebSiteNews(models.Model):
    """
    官网新闻
    """
    title = models.CharField(verbose_name="新闻标题", null=True, max_length=300)
    content = models.TextField(verbose_name='内容')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, null=True)
    sort = models.IntegerField(verbose_name="排序", null=False, default=0)
    top = models.IntegerField(verbose_name="置顶", null=False, default=0)
    hits = models.IntegerField(verbose_name='点击量', null=False, default=0)
    status = models.IntegerField(verbose_name="状态", default=False)
    cover_image = models.CharField(verbose_name="封面图", max_length=200, null=True)
    publish_time = models.DateTimeField(verbose_name='发布时间', null=True)
    deleted = models.BooleanField(verbose_name='是否删除', default=False)
    create_by = models.ForeignKey(User, models.CASCADE, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', null=True, auto_now_add=True)

    class Meta:
        db_table = 'website_news'
        verbose_name_plural = '新闻'