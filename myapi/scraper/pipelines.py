# example_project/open_news/scraper/pipelines.py

from __future__ import unicode_literals
from builtins import str
from builtins import object
import logging
from django.db.utils import IntegrityError
from scrapy.exceptions import DropItem
from scrapy_django_dashboard.models import SchedulerRuntime


class DjangoWriterPipeline(object):

    def process_item(self, item, spider):
        if spider.conf['DO_ACTION']:
            try:
                item['course_website'] = spider.ref_object

                checker_rt = SchedulerRuntime(runtime_type='C')
                checker_rt.save()
                item['checker_runtime'] = checker_rt

                item.save()
                spider.action_successful = True
                spider.logger.info("{cs}Item {id} saved to Django DB.{ce}".format(
                    id=item._id_str,
                    cs=spider.bcolors['OK'],
                    ce=spider.bcolors['ENDC']))

            except IntegrityError as e:
                spider.logger.error(str(e))
                raise DropItem("Missing attribute.")

        return item