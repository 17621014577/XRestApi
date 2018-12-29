# Generated by Django 2.0 on 2018-12-06 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Example', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newscategory',
            options={'verbose_name_plural': '新闻分类'},
        ),
        migrations.AlterModelOptions(
            name='websitenews',
            options={'verbose_name_plural': '新闻'},
        ),
        migrations.AlterField(
            model_name='websitenews',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Example.NewsCategory'),
        ),
    ]