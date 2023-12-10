from django import template

from oscar.core.loading import get_model

register = template.Library()
Product = get_model('catalogue', 'product')
Promotions = get_model('oscar_promotions', 'HandPickedProductList')


@register.simple_tag(name="all_products")
def get_all_products():
    return Product.objects.all()


@register.simple_tag(name="all_promotions")
def get_all_promotions():
    return Promotions.objects.all()
