# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from __future__ import unicode_literals
from scrapy_django_dashboard.spiders.django_spider import DjangoSpider
from myapi.models import CourseWebsite, Course, CourseItem


class CourseSpider(DjangoSpider):

    name = 'course_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(CourseWebsite, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Course
        self.scraped_obj_item_class = CourseItem
        super(CourseSpider, self).__init__(self, *args, **kwargs)