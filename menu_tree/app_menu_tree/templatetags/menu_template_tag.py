from django import template
from django.db.models import QuerySet
from app_menu_tree.models import MenuItem
from typing import Dict

register = template.Library()


@register.filter
def active_items(value: QuerySet):
    return value.filter(active=True)


@register.inclusion_tag('base_parts/menu.html')
def draw_menu(menu_name) -> Dict:
    """
    Вывод меню
    return: context
    """

    menu_items: QuerySet = MenuItem.objects.filter(menu__name=menu_name, active=True)
    context: Dict = {'items': menu_items,
                     'menu_name': menu_name}

    return context
