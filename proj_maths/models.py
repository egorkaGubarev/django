from django.db import models


class Term(models.Model):
    termid = models.AutoField(db_column='termId', primary_key=True)
    term = models.TextField()
    definition = models.TextField()
    author = models.TextField()

    class Meta:
        managed = False
        db_table = 'Terms'
