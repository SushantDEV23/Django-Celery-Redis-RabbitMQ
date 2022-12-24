from django.db import models

class POST(models.Model):
    name = models.CharField(max_length=90)
