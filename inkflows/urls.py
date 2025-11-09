import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

from inkflows import settings

urlpatterns = [
    path("", include("workers.urls")),
    path("admin/", admin.site.urls),
    path("_debug_/", include(debug_toolbar.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path ('auth/', include('djoser.urls')),
    path ('auth/', include('djoser.urls.jwt')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
