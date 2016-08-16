# coding:utf-8
from django.db import models


class Menus(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = verbose_name_plural = 'Menus'

    def __str__(self):
        return self.name
