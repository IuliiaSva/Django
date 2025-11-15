from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkerDetailView, WorkerListView1, WorkerListView2, WorkerViewSet, WorkplacesViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


app_name = "workers"

router = DefaultRouter()
router.register(r"workers", WorkerViewSet)
router.register(r"workplaces", WorkplacesViewSet)

urlpatterns = [
    path("", WorkerListView1.as_view(), name="worker_main"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker_detail"),
    path("worker/", WorkerListView2.as_view(), name="worker_update"),
    path ("api/", include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
