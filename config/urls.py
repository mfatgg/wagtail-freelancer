from django.apps import apps
from django.conf import settings
#from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, re_path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    #re_path(r'search/$', views.search, name='search'),
    #url(r'^api/', include(wagtailapi_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # Oscar's then Wagtail's serving mechanism. This should be the last
    # pattern in the list:

    # FIXME: Oscar Promotions need home page adaption to work (also in app)!
    #path('', apps.get_app_config('oscar_promotions').urls),
    path('dashboard/promotions/', apps.get_app_config('oscar_promotions_dashboard').urls),
    path('', include(apps.get_app_config('oscar').urls[0])),
    path('', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
