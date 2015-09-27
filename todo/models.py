from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    owner = models.ForeignKey(User)
    content = models.CharField(max_length=150, blank=False)
    created_date = models.DateTimeField('Created date', auto_now_add=True)
    moreinfo = models.CharField(max_length=400, blank=True)

    STATUS = (
        (0, 'In Progress'),
        (1, 'Pending'),
        (2, 'Done'),
        (3, 'Cancelled'),
    )
    status = models.IntegerField(choices=STATUS, default=0)

    PRIORITY = (
        (0, 'Low'),
        (1, 'Medium'),
        (2, 'High'),
    )
    priority = models.IntegerField(choices=PRIORITY, default=0)

    def __unicode__(self):
        return self.content
