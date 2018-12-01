from django.apps import AppConfig


class CustomerConfig(AppConfig):
    name = 'Customer'
    verbose_name = '客户'


class NewsCategoryConfig(AppConfig):
    name = 'NewsCategory'


class WebSiteNewsConfig(AppConfig):
    name = 'WebSiteNews'