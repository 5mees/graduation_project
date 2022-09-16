from django.db import models


class GraduateProject(models.Model):
    title = models.CharField(max_length=100)
    content = models.FileField()
    description = models.TextField(null=True)

    def __str__(self):
        return self.title

