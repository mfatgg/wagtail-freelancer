from django import template

from oscar.core.loading import get_model

register = template.Library()
Product = get_model('catalogue', 'product')


@register.simple_tag(name="all_products")
def get_all_products():
    return Product.objects.all()
