from django import template
from reparado.models import Categoria

register = template.Library()

@register.filter
def get_categoria_by_id(categorias, categoria_id):
    try:
        return categorias.get(id=categoria_id).nombre_cat
    except Categoria.DoesNotExist:
        return "N/A"