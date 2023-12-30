from django.db import models


class Type(models.Model):
    title = models.CharField(max_length=60, null=False, blank=False, verbose_name='Название')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = "Type"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Status(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название", unique=True, null=False, blank=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "Status"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Task(models.Model):
    summary = models.CharField(max_length=60, null=False, blank=False, verbose_name='Краткое описание')
    description = models.CharField(max_length=60, blank=True, null=True, verbose_name='Описание')
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    types = models.ManyToManyField('webapp.Type', related_name='tasks', verbose_name='Типы')
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    end_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.pk}. {self.description}'

