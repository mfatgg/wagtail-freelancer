# pylint: disable=W0201

from django.apps import apps
from django.conf import settings
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

from oscar.core.application import OscarConfig
from oscar.core.loading import get_class


class Shop(OscarConfig):
    name = "oscar"

    def ready(self):
        from django.contrib.auth.forms import SetPasswordForm

        self.catalogue_app = apps.get_app_config("catalogue")
        self.customer_app = apps.get_app_config("customer")
        self.basket_app = apps.get_app_config("basket")
        self.checkout_app = apps.get_app_config("checkout")
        self.search_app = apps.get_app_config("search")
        self.dashboard_app = apps.get_app_config("dashboard")
        self.offer_app = apps.get_app_config("offer")
        self.wishlists_app = apps.get_app_config("wishlists")

    def get_urls(self):
        from django.contrib.auth import views as auth_views

        from oscar.views.decorators import login_forbidden

        urls = [
            path("catalogue/", self.catalogue_app.urls),
            path("basket/", self.basket_app.urls),
            path("checkout/", self.checkout_app.urls),
            path("accounts/", self.customer_app.urls),
            path("search/", self.search_app.urls),
            path("dashboard/", self.dashboard_app.urls),
            path("offers/", self.offer_app.urls),
            path("wishlists/", self.wishlists_app.urls),
        ]
        return urls