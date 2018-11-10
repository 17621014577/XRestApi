# Generated by Django 2.1.2 on 2018-10-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
    ]