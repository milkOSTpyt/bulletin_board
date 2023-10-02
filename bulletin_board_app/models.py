from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class City(models.Model):
    name = models.CharField(max_length=70, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Advert(models.Model):
    title = models.CharField(db_index=True, max_length=250, verbose_name='Заголовок объявления')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
