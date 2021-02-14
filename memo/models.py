from django.db import models
from django.utils import timezone

import datetime

class Memo(models.Model):
    memo_title = models.CharField(max_length=200)
    memo_type = models.CharField(max_length=200)
    memo_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    delete = models.DateTimeField('date deleted', null=True, blank=True)

    def __str__(self):
        return self.memo_text
    
    def __str__(self):
        return self.memo_title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Create your models here.
