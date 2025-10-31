from django.db import models


class Workplaces(models.Model):
    number = models.IntegerField("Номер", unique=True)
    other = models.CharField("Дополнительная информация", max_length=100)

    class Meta:
        verbose_name = "рабочее место"
        verbose_name_plural = "Рабочие места"

    def __str__(self):
        return f'Рабочее место №{self.number}'
