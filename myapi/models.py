from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from scrapy_djangoitem import DjangoItem
from scrapy_django_dashboard.models import Scraper, SchedulerRuntime
from six import python_2_unicode_compatible
from django.utils import timezone
from datetime import datetime
from django.utils.translation import gettext_lazy as _


@python_2_unicode_compatible
class CourseWebsite(models.Model):
	name = models.CharField(max_length=200)
	url = models.URLField()
	scraper = models.ForeignKey(
		Scraper, blank=True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(
		SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name



class Course(models.Model) :

	class State(models.TextChoices):
		NEWSOUTHWALES = 'New South Wales', _('New South Wales')
		NORTHERNTERRITORY = 'Northern Territory', _('Northern Territory')
		QUEENSLAND = 'Queensland', _('Queensland')
		SOUTHAUSTRALIA = 'South Australia', _('South Australia')
		TASMANIA ='Tasmania', _('Tasmania')
		VICTORIA ='Victoria', _('Victoria')
		WESTERNAUSTRALIA ='Western Australia', _('Western Australia')
		AUSTRALIANCAPITOLTERRITORY ='Australian Capital Territory', _('Australian Capital Territory')
	
	title = models.CharField(max_length=200)
	course_website = models.ForeignKey(
		CourseWebsite, blank=True, null=True, on_delete=models.SET_NULL)
	university = models.CharField(max_length=60, blank=True)
	state = models.CharField(
		max_length=30,
		choices=State.choices,
		default=State.VICTORIA,
	)
	campus = models.CharField(max_length=60, blank = True)
	description = models.TextField(blank=True)
	learningOutcomes = models.TextField(blank=True)
	fees = models.DecimalField(max_digits=8, decimal_places=2, default='0', blank = True)
	yearlyFees = models.DecimalField(max_digits=8, decimal_places=2, default='0', blank = True)
	guaranteedAtar = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
	duration = models.DecimalField(max_digits=4, decimal_places=2, default = '3')
	units = models.DecimalField(max_digits=5, decimal_places=2, default = '24')
	uniRanking = models.DecimalField(max_digits=8, decimal_places=2, default = '69')
	url = models.URLField(blank=True)
	idUrl = models.URLField(blank=True)
	dateTimeScraped = models.DateTimeField(default=datetime.now, blank=True)
	checker_runtime = models.ForeignKey(
		SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.title


class CourseItem(DjangoItem):
	django_model = Course


@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
	if isinstance(instance, CourseWebsite):
		if instance.scraper_runtime:
			instance.scraper_runtime.delete()

	if isinstance(instance, Course):
		if instance.checker_runtime:
			instance.checker_runtime.delete()


pre_delete.connect(pre_delete_handler)

