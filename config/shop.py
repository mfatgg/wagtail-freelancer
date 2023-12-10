# pylint: disable=W0201

from django.apps import apps
from django.conf import settings
from django.urls import path, reverse_lazy, re_path
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import RedirectView

from oscar.core.application import OscarConfig
from oscar.core.loading import get_class, get_model


class ShopConfig(OscarConfig):
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


class PromotionsConfig(OscarConfig):

    label = 'oscar_promotions'
    name = 'oscar_promotions'
    verbose_name = _("Promotions")

    namespace = 'promotions'

    def ready(self):
        super().ready()
        self.home_view = get_class('oscar_promotions.views', 'HomeView', module_prefix='oscar_promotions')
        self.record_click_view = get_class(
            'oscar_promotions.views', 'RecordClickView', module_prefix='oscar_promotions'
        )

    def get_urls(self):
        PagePromotion = get_model('oscar_promotions', 'PagePromotion')
        KeywordPromotion = get_model('oscar_promotions', 'KeywordPromotion')
        urls = [
            re_path(
                r'page-redirect/(?P<page_promotion_id>\d+)/$',
                self.record_click_view.as_view(model=PagePromotion),
                name='page-click',
            ),
            re_path(
                r'keyword-redirect/(?P<keyword_promotion_id>\d+)/$',
                self.record_click_view.as_view(model=KeywordPromotion),
                name='keyword-click',
            ),
            #re_path(r'^$', self.home_view.as_view(), name='home'),
        ]
        return self.post_process_urls(urls)
