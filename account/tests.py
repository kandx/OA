# -*- coding: utf-8 -*-
from django.test import TestCase
from models import Profile, Department, Duty, Level, Character
from django.contrib.auth.models import User
# Create your tests here.

class ProfileMethodTest(TestCase):
	
	def setUp(self):
		user = User.objects.get(email__contains="kandx")
		depart = Department.objects.create(name="建设开发处")
		duty = Duty.objects.create(name="副处长")
		level = Level.objects.create(name="副主任科员")
		character = Character.objects.create(name="公务员")
		profile = Profile.objects.create(gender="M", birthday="1982-1-8", begin_work_date="2006-7-1",
			department=depart, duty=duty, user=user, level=level, enter_date="2013-4-23",
			character=character)

	def test_holidays_property(self):
		profile = Profile.objects.get(birthday="1982-1-8")
		self.assertEqual(profile.holidays, 5)

