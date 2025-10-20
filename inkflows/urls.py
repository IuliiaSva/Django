import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from inkflows import settings

urlpatterns = [
    path("", include("workers.urls")),
    path("admin/", admin.site.urls),
    path("_debug_/", include(debug_toolbar.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
