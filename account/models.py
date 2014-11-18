# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Department(models.Model):
    class Meta:
        verbose_name = "处室"
        verbose_name_plural = "处室"
        db_table = "cbd_department"

    name = models.CharField(max_length=10, verbose_name="处室名称")
    create_time = models.DateTimeField(auto_now_add=True) 

    def __unicode__(self):
    	return self.name    

class Duty(models.Model):
    class Meta:
        verbose_name = "职务"
        verbose_name_plural = "职务"
        db_table = "cbd_duty"

    name = models.CharField(max_length=5, verbose_name="职务名称")
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Level(models.Model):
    class Meta:
        verbose_name = "级别"
        verbose_name_plural = "级别"
        db_table = "cbd_level"

    name = models.CharField(max_length=5, verbose_name="级别名称")
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
    
class Character(models.Model):
    class Meta:
        verbose_name = "人员性质"
        verbose_name_plural = "人员性质"
        db_table = "cbd_character"

    name = models.CharField(max_length=5,verbose_name="人员类型")
    create_time = models.DateTimeField()

    def __unicode__(self):
        return self.name
    


class Profile(models.Model):
	"""
	定义用户信息字段，包括以下内容：
	性别、生日、开始工作时间、进入本单位时间、所在处室、职务、级别、工作性质等字段
	"""
	class Meta:
		verbose_name = "个人信息"
		verbose_name_plural = "个人信息"
		db_table = "cbd_profile"

	SEX = (
		('M', '男'),
		('F', '女'),
		)
	gender = models.CharField(max_length=1, choices=SEX, verbose_name="性别")
	birthday = models.DateField(verbose_name="生日")
	enter_date = models.DateField(verbose_name="进入本单位时间")
	begin_work_date = models.DateField(verbose_name="开始工作时间")
	user = models.OneToOneField(User, verbose_name="账号信息")
	department = models.ForeignKey(Department, verbose_name="部门")
	duty = models.ForeignKey(Duty, verbose_name="职务")
	level = models.ForeignKey(Level, verbose_name="级别")
	character = models.ForeignKey(Character, verbose_name="人员性质")

	def __unicode__(self):
		return "%s %s" % (self.user.first_name, self.user.last_name)

	def _get_holidays(self):
		start_work_date = datetime.strptime(self.begin_work_date, '%Y-%m-%d')
		now = datetime.now()
		timedelta = now-start_work_date
		years = timedelta.days()/365
		if years<10:
			return 5
		elif years>=10 and years<15:
			return 10
		else:
			return 15
	holidays = property(_get_holidays)
	

