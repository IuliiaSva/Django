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
class Images(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    order = models.PositiveIntegerField(default=0, blank=True, null=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    class Meta:
        ordering = ['order',]
        verbose_name = 'Изображение сотрудника'
        verbose_name_plural = ('Изображения сотрудника')

    def save(self, *args, **kwargs):
        if not self.order:
            last_order = Images.objects.filter(employee=self.worker).order_by('-order').first()
            self.order = last_order.order + 1 if last_order else 1
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Изображение для {self.worker.name} (Порядок: {self.order})"


# Create your models here.
