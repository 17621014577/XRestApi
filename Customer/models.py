from django.db import models

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

