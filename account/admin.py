# -*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Permission
from models import Department, Duty, Level, Character, Profile

# Register your models here.
admin.site.register(Department)
admin.site.register(Duty)
admin.site.register(Level)
admin.site.register(Character)
admin.site.register(Profile)
admin.site.register(Permission)

