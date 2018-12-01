from django.contrib import admin
 
# Register your models here.
from Customer import models
admin.site.register(models.Customer)
admin.site.register(models.NewsCategory)
admin.site.register(models.WebSiteNews)
