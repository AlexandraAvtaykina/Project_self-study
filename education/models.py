from django.db import models

from users.models import User

NULLABLE = {'blank': 'True', 'null': 'True'}


class Section(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name='название раздела')

    image = models.ImageField(upload_to='section/',
                              verbose_name='картинка раздела',
                              **NULLABLE)

    description = models.TextField(verbose_name='описание раздела',
                                   **NULLABLE)

    date_create = models.DateField(verbose_name='дата создания',
                                   auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Material(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name='название материала')

    description = models.TextField(verbose_name='описание материала',
                                   **NULLABLE)

    image = models.ImageField(upload_to='material/',
                              verbose_name='картинка материала',
                              **NULLABLE)

    url = models.URLField(verbose_name='ссылка на видео',
                          **NULLABLE)

    section = models.ForeignKey(Section,
                                on_delete=models.CASCADE,
                                verbose_name='ссылка на раздел',
                                **NULLABLE)

    date_create = models.DateField(verbose_name='дата создания',
                                   auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
