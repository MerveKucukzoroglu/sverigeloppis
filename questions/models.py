from django.db import models
from loppises.models import Loppis

class Questions(models.Model):

    loppis = models.ForeignKey(Loppis, on_delete=models.CASCADE, related_name='questions')
    author = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'Questions'


    def __str__(self):
        return f"Question {self.content} by {self.author}"
