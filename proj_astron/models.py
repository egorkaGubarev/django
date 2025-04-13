from django.db import models


class Star(models.Model):
    star = models.TextField(primary_key=True)
    type = models.TextField()
    magnitude = models.FloatField()
    constellation = models.TextField()

    class Meta:
        managed = False
        db_table = 'Stars'

    objects = models.Manager()
