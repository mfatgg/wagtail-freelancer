from django.apps import apps
from django.urls import path

from oscar import config


class MyShop(config.Shop):
    # Override get_urls method
    def get_urls(self):
        urlpatterns = super(MyShop, self).get_urls()[1:]
        urlpatterns.append(path('promotions/', apps.get_app_config("oscar_promotions").urls))
        urlpatterns.append(path('dashboard/promotions/', apps.get_app_config("oscar_promotions_dashboard").urls))
        return urlpatterns
