# -*- coding: utf-8 -*-
from django.db import models
import time


class Document(models.Model):
    title = models.CharField(max_length=256, default='defTitle', unique=True)
    docfile = models.FileField(upload_to='documents/' +str(int(time.time())))

class Site(models.Model):
	url = models.CharField(max_length=400, default='defURL', unique=True)