from __future__ import unicode_literals
from django.contrib import admin
from .models import CourseWebsite
from .models import Course

class CourseWebsiteAdmin(admin.ModelAdmin): #displays more columns in admin interface, for course website model
    list_display = ('id', 'name', 'url', 'scraper')
    list_display_links = ('name',)
    search_fields = ['id', 'name', 'url', 'scraper']

    #def url_(self, instance): code from scrapy django dashboard, surrounds url in href
    #    return '<a href="{url}" target="_blank">{title}</a>'.format(
     #       url=instance.url, title=instance.url)
   # url_.allow_tags = True


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'university', 'campus', 'state', 'guaranteedAtar', 'fees', 'yearlyFees', 'duration', 'url', 'units', 'idUrl', 'uniRanking')
    list_display_links = ('title',)
    raw_id_fields = ('checker_runtime',)
    search_fields = ['title', 'id', 'title','university', 'campus', 'state', 'guaranteedAtar', 'fees', 'yearlyFees', 'duration', 'units', 'url', 'dateTimeScraped', 'idUrl', 'uniRanking' ]
    
   

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseWebsite, CourseWebsiteAdmin)



