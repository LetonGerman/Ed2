from django.db import models


class GrantYears(models.Model):
    year = models.SmallIntegerField()
    desc = models.TextField()
