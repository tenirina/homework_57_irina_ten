from django.db import models


class Issue(models.Model):
    summary = models.CharField(verbose_name='Summary', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name="Description", max_length=1000, null=True)
    created_at = models.DateTimeField(verbose_name='Date of created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date of updates', auto_now=True)
    status = models.ForeignKey(verbose_name="Status", to='webapp.Status', related_name='issue', on_delete=models.CASCADE)
    type = models.ManyToManyField(to='webapp.Type', through='webapp.IssueType', through_fields=('issue', 'type'), related_name='issue', default='task')
