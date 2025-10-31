from django.utils import timezone

from cfgv import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from workplaces.models import Workplaces


class Worker(models.Model):

    date_of_joining = models.DateField("Дата приема", null=True,
      blank=True,)
    gender = models.CharField("пол", max_length=100)
    name = models.CharField("ФИО", max_length=100)
    skills = models.CharField("Навыки", max_length=100)
    grade = models.IntegerField(
        "Уровень освоения навыка",
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    description = models.CharField("Описание", max_length=100)
    workplace = models.OneToOneField(
        Workplaces,
        on_delete=models.CASCADE,
        related_name="worker",
        null=True,
        blank=True,
    )

    def clean(self):
        if self.workplace:
            adjacent_workplaces = Workplaces.objects.filter(
                number__in=[self.workplace.number - 1,
                            self.workplace.number + 1]
            )
            for adjacent_place in adjacent_workplaces:
                neighboring_workers = Worker.objects.filter(workplace=adjacent_place)
                for worker in neighboring_workers:
                    if (self.skills == 'бекендер' and
                        worker.skills == 'тестировщик') or \
                        (self.skills == 'тестировщик' and
                         worker.skills == 'бекендер') or \
                         (self.skills == 'фронтендер' and
                          worker.skills == 'тестировщик') or \
                          (self.skills == 'тестировщик' and
                           worker.skills == 'фронтендер'):
                        raise ValidationError(
                            'Разработчик и тестировщик не могут сидеть рядом.'
                        )

    def get_days_worked(self):
        if self.date_of_joining:
            today = timezone.now().date()
            return (today - self.date_of_joining).days
        return 0

    class Meta:
        verbose_name = "работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return self.name


class Images(models.Model):

    image = models.ImageField(upload_to="images/", blank=True)
    order = models.PositiveIntegerField(default=0, blank=True, null=True)
    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE,
        related_name="images", null=True, blank=True
    )

    class Meta:
        ordering = [
            "order",
        ]
        verbose_name = "Изображение сотрудника"
        verbose_name_plural = "Изображения сотрудника"

    def save(self, *args, **kwargs):
        if not self.order:
            last_order = (
                Images.objects.filter(worker=self.worker).
                order_by("-order").first()
            )
            self.order = last_order.order + 1 if last_order else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Изображение для {self.worker.name} (Порядок: {self.order})"
