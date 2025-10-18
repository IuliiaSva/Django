from django.db import models
from workplaces.models import Workplaces


class Worker(models.Model):
    gender = models.CharField('пол',max_length=100)
    name = models.CharField('ФИО',max_length=100)
    skills = models.CharField('Навыки',max_length=100)
    grade = models.CharField('Уровень освоения навыка',max_length=10)
    discription = models.CharField('Описание',max_length=100)
    workplace = models.OneToOneField(Workplaces, on_delete=models.CASCADE,  related_name='worker', null=True, blank=True)
    class Meta:
        verbose_name = 'работник'
        verbose_name_plural = ('Работники')
    def __str__(self):
       return self.name


# Create your models here.
