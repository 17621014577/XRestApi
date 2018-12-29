# Generated by Django 2.0 on 2018-12-06 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='姓名')),
                ('sex', models.IntegerField(default=1)),
                ('age', models.IntegerField(blank=True, default=30, null=True)),
                ('tel', models.CharField(default='', max_length=50, null=True)),
                ('passwd', models.CharField(default='', max_length=100, null=True)),
                ('qq', models.CharField(default='', max_length=20, null=True)),
                ('weixin', models.CharField(default='', max_length=30, null=True)),
                ('e_mail', models.CharField(default='', max_length=50, null=True)),
                ('title', models.TextField(blank=True, default='', null=True, verbose_name='头衔')),
                ('image', models.CharField(default='', max_length=255, null=True, verbose_name='头像')),
                ('company', models.CharField(default='', max_length=100, null=True, verbose_name='公司名称')),
                ('com_addr', models.CharField(default='', max_length=300, null=True, verbose_name='公司地址')),
                ('com_type', models.CharField(default='', max_length=300, verbose_name='公司类型')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30, null=True, verbose_name='分类名称')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'news_category',
            },
        ),
        migrations.CreateModel(
            name='WebSiteNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True, verbose_name='新闻标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('top', models.IntegerField(default=0, verbose_name='置顶')),
                ('hits', models.IntegerField(default=0, verbose_name='点击量')),
                ('status', models.IntegerField(default=False, verbose_name='状态')),
                ('cover_image', models.CharField(max_length=200, null=True, verbose_name='封面图')),
                ('publish_time', models.DateTimeField(null=True, verbose_name='发布时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Example.NewsCategory')),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'website_news',
            },
        ),
    ]
