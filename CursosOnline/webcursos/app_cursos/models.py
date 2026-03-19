from django.db import models

class Cursos(models.Model):
    title = models.CharField(verbose_name='Título', max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False) 
    description = models.CharField(verbose_name='Descrição', null=False, blank=False)