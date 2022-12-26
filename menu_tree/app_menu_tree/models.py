from django.db import models
from django.core.exceptions import ValidationError


class Menu(models.Model):
    """
    Модель для различных меню. В данной реализации содержит только имя меню.
    """

    name = models.CharField(verbose_name='name', max_length=255)

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'
        ordering = ['name']

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Модель составных пунктов древоводиного меню. Включает ссылку на родителя.
    """

    name = models.CharField(verbose_name='name', max_length=255)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', verbose_name='menu item')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                               verbose_name='parent')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="url")
    active = models.BooleanField(verbose_name='active', default=True)

    class Meta:
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'
        ordering = ['name']

    def clean(self):
        if self.menu != self.parent.menu:
            raise ValidationError(
                {'parent': f"Element and its parent should be in same menu. Parent's menu: {self.parent.menu}"}
            )

    def __str__(self):
        return self.name
