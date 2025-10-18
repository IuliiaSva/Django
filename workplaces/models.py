from django.db import models

class Workplaces(models.Model):
    number = models.CharField('Номер',max_length=100)
    other = models.CharField('Дополнительная информация',max_length=100)
    class Meta:
        verbose_name = 'рабочее место'
        verbose_name_plural = ('Рабочие места')
    def __str__(self):
        return self.number