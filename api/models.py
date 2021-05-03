from django.db import models


class Tasks(models.Model):
    link = models.TextField(blank=False)
    level = models.IntegerField(blank=False, null=True)
    status = models.TextField(default='in_work')

    def __str__(self):
        return self.status
